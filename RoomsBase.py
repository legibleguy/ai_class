from enum import Enum

class Action(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    SUCK = 5

actionDir = {
    Action.UP : [0, -1],
    Action.DOWN : [0, 1],
    Action.LEFT : [-1, 0],
    Action.RIGHT : [1, 0],
    Action.SUCK : [0, 0]
}

actionCost = {
    Action.UP : 0.8,
    Action.DOWN : 0.7,
    Action.LEFT : 1.0,
    Action.RIGHT : 0.9,
    Action.SUCK : 0.6
}


class Room:
    isDirty = False
    x = 0
    y = 0
    neighbors = {} 
    def __init__(self, inx, iny, boundsX=-1, boundsY=-1):
        self.x = inx
        self.y = iny
        if self.x > 1:
            self.neighbors[self.x-1, self.y] = actionCost[Action.LEFT] #neighbor on the left
        if self.x < boundsX:
            self.neighbors[self.x+1, self.y] = actionCost[Action.RIGHT] #neighbor on the right
        if self.y > 1:
            self.neighbors[self.x, self.y-1] = actionCost[Action.UP] #neighbor above
        if self.y < boundsY:
            self.neighbors[self.x, self.y+1] = actionCost[Action.DOWN] #neighbor below 

def debugRooms(inRooms, currentLocation=[0,0]):
    print("\n")
    toPrint = ""
    currLocIndicator = " "
    lastY = inRooms[0].y
    for room in inRooms:
        if(room.y != lastY):
            toPrint += "\n"
            lastY = room.y
        toPrint += "|"
        if currentLocation[0] == room.x and currentLocation[1] == room.y: currLocIndicator = "*"
        else: currLocIndicator = " "
        if room.isDirty:
            toPrint += "(" + str(room.x) + ", " + str(room.y) + ")"+currLocIndicator+"d"
        else:
            toPrint += "(" + str(room.x) + ", " + str(room.y) + ")"+currLocIndicator+" "
        toPrint += "|\t"
    print(toPrint)