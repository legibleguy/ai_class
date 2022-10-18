class graph:
    def __init__(self, x, y):
        self.size = [x, y]
        self.rooms = {}
        for iny in range(0, y):
            for inx in range(0, x):
                self.rooms[inx+1, iny+1] = False

    def isEverythingClean(self) -> bool:
        for r in self.rooms:
            if self.rooms[r] == True: return False

        return True

    def setDirtyRooms(self, inRooms):
        for room in inRooms:
            self.rooms[room[0], room[1]] = True
    
    def __str__(self) -> str:
        for r in self.rooms:
            print(str(r) + " - " + str(self.rooms[r]))

def debugGraph(inGraph : graph, currentLocation=[0,0]):
    toPrint = ""
    currLocIndicator = " "
    lastY = inGraph.size[1]
    for room in inGraph.rooms:
        if(room[1] != lastY):
            toPrint += "\n"
            lastY = room[1]
        toPrint += "|"
        if currentLocation[0] == room[0] and currentLocation[1] == room[1]: currLocIndicator = "*"
        else: currLocIndicator = " "
        if inGraph.rooms[room] == True:
            toPrint += "(" + str(room[0]) + ", " + str(room[1]) + ")"+currLocIndicator+"d"
        else:
            toPrint += "(" + str(room[0]) + ", " + str(room[1]) + ")"+currLocIndicator+" "
        toPrint += "|\t"
    print(toPrint)