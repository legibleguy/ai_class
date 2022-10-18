import copy
import time
from GraphBase import graph
from NodeBase import Node
from ActionsBase import Action

def getActionsAtLocation(loc, inGraph : graph):
    actions = []
    if inGraph.rooms[loc[0], loc[1]] == True:
        actions.append(Action.SUCK)
    if loc[0] > 1:
        actions.append(Action.LEFT)
    if loc[1] > 1:
        actions.append(Action.UP)
    if loc[0] < inGraph.size[0]:
        actions.append(Action.RIGHT)
    if loc[1] < inGraph.size[1]:
        actions.append(Action.DOWN)
    return actions

def expandNode(inNode=Node()):
    actions = getActionsAtLocation(inNode.location, inNode.state)
    nodesOut = []
    for a in actions:
        if a == Action.SUCK:
            newGraph = copy.deepcopy(inNode.state)
            newGraph.rooms[inNode.location[0], inNode.location[1]] = False
            newNode = Node(inNode, a, [0,0], newGraph)
            nodesOut.append(newNode)
        if a == Action.LEFT:
            newGraph = copy.copy(inNode.state)
            newNode = Node(inNode, a, [-1,0],newGraph)
            nodesOut.append(newNode)
        if a == Action.RIGHT:
            newGraph = copy.copy(inNode.state)
            newNode = Node(inNode, a, [1,0],newGraph)
            nodesOut.append(newNode)
        if a == Action.UP:
            newGraph = copy.copy(inNode.state)
            newNode = Node(inNode, a, [0,-1],newGraph)
            nodesOut.append(newNode)
        if a == Action.DOWN:
            newGraph = copy.copy(inNode.state)
            newNode = Node(inNode, a, [0,1],newGraph)
            nodesOut.append(newNode)
    return nodesOut

#note theat this Uniform Cost function can act as both Tree search and Graph search depending on what you set the treeSearch parameter to
#returns a node that leads to success (in out case, all clean rooms) with the smallest path cost
def UniformCostSearch(inGraph : graph, initialPos, treeSearch = False, firstNodes = [], increated = [0],  inexpanded = [0]) -> Node:
    startTime = time.time()
    start = Node()
    start.location = initialPos
    start.state = inGraph
    toVisit=[start]
    visited=[]
    count = 0 #to keep track of the first five nodes
    expandTarget : Node = start
    if inGraph.isEverythingClean(): return start
    else:
        while len(toVisit) > 0:

            expandTarget = toVisit[0]

            #picking the cheapest path here
            if len(toVisit) > 1: 
                for node in toVisit:
                    if node.cost < expandTarget.cost:
                        expandTarget = node
                    
                    #tie
                    elif node.cost == expandTarget.cost:
                        if node.location[1] == expandTarget.location[1]:
                            if node.location[0] < expandTarget.location[0]:
                                expandTarget = node
                        elif node.location[1] < expandTarget.location[1]:
                            expandTarget = node

            #debugging
            if count < 5:
                firstNodes.append(expandTarget)
                count += 1

            #we may terminate earlier here if we reach a node that has all the clean rooms in it
            #otherwise the function will return as soon as the toVisit array is empty
            #or if the execution time goes over an hour
            if expandTarget.state.isEverythingClean() or (time.time() - startTime) > 3600:
                return expandTarget
            
            inexpanded[0] = inexpanded[0] + 1
            newNodes = expandNode(expandTarget)
            increated[0] = increated[0] + len(newNodes) #note that in case of graph search, not all of these generated nodes will be added to the queue.
            if(not treeSearch): visited.append(expandTarget)
            toVisit.remove(expandTarget)

            for node in newNodes:
                if treeSearch or (not (node in visited)):
                    toVisit.append(node)
                elif node in visited: #if the node is visited, we will only allow going into the same state if it's cheaper than before
                    idx = visited.index(node)
                    if visited[idx].cost > node.cost:
                        visited.remove(node)
                        toVisit.append(node)
        return expandTarget
    