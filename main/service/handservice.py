import random

from injector import provider

from main.model.enums import Side, Speed, Height


class BackHandService(object):

    @provider
    def respond_play(self, play: dict) -> dict:
        count = play['count']
        count += 1
        side = random.choice(list(Side)).value
        speed = random.choice(list(Speed)).value
        height = random.choice(list(Height)).value
        return_dict = dict(incomingSide=Side.LEFT.value, effect=False, innerSide=side, count=count, speed=speed,
                           height=height)
        print("[x] Backhand responding play", return_dict)
        return return_dict


class ForeHandService(object):

    def respond_play(self, play: dict) -> dict:
        count = play['count']
        count += 1
        side = random.choice(list(Side)).value
        speed = random.choice(list(Speed)).value
        height = random.choice(list(Height)).value
        other_play = dict(incomingSide=Side.LEFT.value, effect=False, innerSide=side, count=count, speed=speed,
                    height=height)
        print("[x] Forehand responding play: ", other_play)
        return other_play

    def serve(self) -> dict:
        print("[x] Forehand serving")
        side = random.choice(list(Side)).value
        speed = random.choice(list(Speed)).value
        height = random.choice(list(Height)).value
        other_play = dict(incomingSide=Side.LEFT.value, effect=False, innerSide=side, count=0, speed=speed,
                          height=height)
        print("[x] Forehand responding play: ", other_play)
        return other_play
