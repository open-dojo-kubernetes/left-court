from main.service.features.Feature import Features
from main.service.handservice import ForeHandService, BackHandService
from main.service.notifiers.score import ScoreNotifier

from main.service.play.play_handler import PlayHandler

feature_mock = Features()
score_notifier_mock = ScoreNotifier()
backhand_service_mock = BackHandService()
forehand_service_mock = ForeHandService()
handler = PlayHandler()


def test_play_handler_receive_play_correct():
    incoming_play = dict(incomingSide='RIGHT', effect=False, innerSide='RIGHT', count=0, speed='AVG', height='LOW')
    response_play = handler.receive_play(play=incoming_play)
    assert response_play['incomingSide'] == 'LEFT'
    assert response_play['effect']
    assert response_play['count'] == 1
