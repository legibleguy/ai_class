from RoomsBase import Room
from RoomsBase import Action
from RoomsBase import actionCost
from RoomsBase import actionDir

class searchAlg:
    currScore = 0.0
    rooms = []
    visited = []
    sizeX = 0
    sizeY = 0
    currLoc = [0,0]
    def __init__(self, inSizeX, inSizeY):
        self.sizeX = inSizeX
        self.sizeY = inSizeY

        for y in range(0, self.sizeX):
            for x in range(0, self.sizeY):
                self.rooms.append(Room(x+1, y+1, self.sizeX, self.sizeY))
    
    def setDirtyRooms(self, dirtyRooms=[]):
        for room in self.rooms:
            for dirtyRoom in dirtyRooms:
                if room.x == dirtyRoom[0] and room.y == dirtyRoom[1]:
                    room.isDirty = True
                    break
    
    def setAgentLocation(self, x, y):
        self.currLoc = [x,y]
    
    def offsetAgent(self, deltaX, deltaY):
        self.currLoc[0] += deltaX
        self.currLoc[1] += deltaY
    
    def areAllRoomsClean(self) -> bool:
        for room in self.rooms:
            if room.isDirty: return False
        return True
    
    def setRoomClean(self, x, y):
        for room in self.rooms:
            if room.x == x and room.y == y: room.isDirty = False

    # get room, used for adding neighbors of current loaction room to queue
    def getCurrentRoom(self, x, y):
        for room in self.rooms:
            if room.x == x and room.y == y:
                return room


    def doAction(self, inAction):
        self.currScore -=  actionCost[inAction]
        self.offsetAgent(actionDir[inAction])
    
    def runSearch(self) -> None:
        pass

#code below is just to test it out
# from RoomsBase import debugRooms
# testgraph = searchAlg(5,4)
# testgraph.setAgentLocation(3,4)
# testgraph.setDirtyRooms([[1,2],[2,4],[3,5]])
# debugRooms(testgraph.rooms, testgraph.currLoc)