from GraphBase import graph
from ActionsBase import Action
from ActionsBase import actionCost

class Node:

    def __init__(self, inNode=0, action=Action.NONE, offset=[0,0], graphRef=0):
        if inNode != 0:
            self.parent = inNode
            self.cost = inNode.cost + actionCost[action]
            self.action = action
            self.state = graphRef
            self.location = [inNode.location[0] + offset[0], inNode.location[1] + offset[1]]
        else:
            self.action = Action.NONE
            self.parent : Node
            self.cost = 0.0
            self.state : graph
            self.location = [0,0]
    
    #this needs to be implemented,
    #otherwise statements like "is node in visited" will not work
    #because python wouldn't know how to compare node objects
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Node):
            return NotImplemented
        else:
            sameLoc : bool = self.location == __o.location
            sameGraph : bool = self.state.rooms == __o.state.rooms
            return sameLoc and sameGraph

    def __str__(self) -> str:
        return str(self.location)
    
    #this is mostly for debugging purposes
    def getPath(self) -> str:
        fullPath = str(self.location)
        if hasattr(self, 'parent'):
            sucking = ''
            if self.action == Action.SUCK: sucking = "(sucking)"
            fullPath += sucking + " <- " + self.parent.getPath()
            return fullPath
        else:
            return str(self.location)
    
    def getMoves(self) -> str:
        fullPath = str(self.action)
        if hasattr(self, 'parent'):
            fullPath += " <- " + self.parent.getMoves()
            return fullPath
        else:
            return str(self.action)
    
    def getTotalNumNodes(self) -> int:
        if hasattr(self, 'parent'):
            return 1 + self.parent.getTotalNumNodes()
        else: return 1
