import requests
from injector import inject, Injector

from service.handservice import BackHandService
from service.handservice import ForeHandService
from service.notifiers.score import ScoreNotifier


class PlayHandler(object):
    @staticmethod
    def get_right_side_host() -> str:
        return "http://localhost:8080"

    @staticmethod
    def get_right_health_check() -> str:
        return PlayHandler.get_right_side_host() + "/actuator/health"

    @staticmethod
    def get_right_play() -> str:
        return PlayHandler.get_right_side_host() + "/right/play"

    @inject
    def __init__(self):
        injector = Injector()
        self.score_notifier = injector.get(ScoreNotifier)
        self.backhand_service = injector.get(BackHandService)
        self.forehand_service = injector.get(ForeHandService)

    def start_service(self):
        """
        This will start to serve, and call the other Micro Service until the point is given or taken
        :return:
        """
        return self.__keep_playing()

    def receive_play(self, play: dict) -> dict:
        """
        This will respond the plays until the point is given or taken
        :return:
        """
        if 'error' in play.keys():
            print('Error caught ', play['error'])
            return play
        else:
            print('Received ', play)
        if (play['innerSide'] == 'OUTSIDE').__or__(play['innerSide'] == 'NET'):
            self.score_notifier.notify_my_point(play['count'])
            return {'error':'Point for left side, ball did not hit left side table', 'errorCode': 100010}
        elif (play['height'] == 'BEYOND_REACH').__or__(play['speed'] == 'OMFG'):
            self.score_notifier.notify_foe_point(play['count'])
            return {'error': 'Point for right side, ball could not be reachable', 'errorCode': 100011}
        elif play['innerSide'] == 'RIGHT':
            return self.backhand_service.respond_play(play)
        elif play['innerSide'] == 'LEFT':
            return self.forehand_service.respond_play(play)
        else:
            return {"error": "unknown place for continue play ", "errorCode": 100002}

    def __keep_playing(self):
        play_list = []
        my_play = self.forehand_service.serve()
        foe_play = self.send_to_other_side(my_play)
        play_list.append(my_play)
        play_list.append(foe_play)
        while (not 'error' in foe_play.keys()).__and__(not 'error' in my_play.keys()):
            foe_play = self.send_to_other_side(my_play)
            my_play = self.receive_play(foe_play)
            play_list.append(my_play)
            play_list.append(foe_play)
        print('Plays ', play_list.__len__())
        return play_list

    def send_to_other_side(self, play: dict) -> dict:
        print('Sending play ', play)
        other_play = requests.post(PlayHandler.get_right_play(), json=play)
        print('Receiving play ', other_play.json())
        return other_play.json()
        # check = requests.get(PlayHandler.get_right_health_check())
        # if check.status_code == 200:
        #     other_play = requests.post(PlayHandler.get_right_play(), data=play)
        #     return other_play.json()
        # else:
        #     return {'error': 'no right side player, I cant play for myself', 'code': 100003}
