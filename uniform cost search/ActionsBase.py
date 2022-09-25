from enum import Enum

class Action(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    SUCK = 5
    NONE = 6

actionDir = {
    Action.UP : [0, -1],
    Action.DOWN : [0, 1],
    Action.LEFT : [-1, 0],
    Action.RIGHT : [1, 0],
    Action.SUCK : [0, 0],
    Action.NONE : [0, 0]
}

actionCost = {
    Action.UP : 0.8,
    Action.DOWN : 0.7,
    Action.LEFT : 1.0,
    Action.RIGHT : 0.9,
    Action.SUCK : 0.6,
    Action.NONE : 0.0
}