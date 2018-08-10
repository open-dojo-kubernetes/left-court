from enum import Enum
from random import random


class Height(str, Enum):
    BURNT = 'BURNT'
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    BEYOND_REACH = 'BEYOND_REACH'


    @staticmethod
    def random():
        return random.choice(list(Height))


class Side(str, Enum):
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    NET = 'NET'
    OUTSIDE = 'OUTSIDE'

    @staticmethod
    def random():
        return random.choice(list(Side))


class Speed(str, Enum):
    SLOW = 'SLOW'
    AVG = 'AVG'
    FAST = 'FAST'
    OMFG = 'OMFG'


    @staticmethod
    def random():
        return random.choice(list(Speed))

