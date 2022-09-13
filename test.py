from contextlib import nullcontext
from enum import Enum

class Action(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    SUCK = 5

class coord:
    x = int()
    y = int()

    def __init__(self, inX, inY):
        x = inX
        y = inY

    def __init__(self):
        x = 0
        y = 0

actionCost = {
    Action.UP : 0.8,
    Action.DOWN : 0.7,
    Action.LEFT : 1.0,
    Action.RIGHT : 0.9,
    Action.SUCK : 0.6
}

class Room:
    dirty = False
    location = coord()
    neighbors = {}

    def __init__(self):
        location = coord()
        dirty = False
    
    def __init__(self, inx, iny):
        coord(inx, iny)

allRooms = []

def generateRooms(numX, numY):
    for roomX in range(numX):
        for roomY in range(numY):
            newRoom = Room(roomX, roomY, False)
            allRooms.append(newRoom)

def getRoomAtCoord(inCoord = coord()) -> Room:
    for r in allRooms:
        if r.location.x == inCoord.x or r.location.y == inCoord.y:
            return r
    return nullcontext

def findNeighbors():
    for r in allRooms:
        # neighbor up
        maybeNeighbor = getRoomAtCoord(r.location.x, r.location.y-1)
        if maybeNeighbor != nullcontext:
            r.neighbors.append({Action.UP : maybeNeighbor})
        #neighbor down
        maybeNeighbor = getRoomAtCoord(r.location.x, r.location.y+1)
        if maybeNeighbor != nullcontext:
            r.neighbors.append({Action.DOWN : maybeNeighbor})
        #neighbor right
        maybeNeighbor = getRoomAtCoord(r.location.x+1, r.location.y)
        if maybeNeighbor != nullcontext:
            r.neighbors.append({Action.RIGHT : maybeNeighbor})
        #neighbor left
        maybeNeighbor = getRoomAtCoord(r.location.x-1, r.location.y+1)
        if maybeNeighbor != nullcontext:
            r.neighbors.append({Action.LEFT : maybeNeighbor})

generateRooms(4, 5)
#findNeighbors()

#print(getRoomAtCoord(1,1).x)
        