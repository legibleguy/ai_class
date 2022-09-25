import timeit

from GraphBase import searchAlg
from RoomsBase import debugRooms


# used during testing in order to create graphs for search to test
# in final version idt_search_run can just be passed a graph directly
def idt_search_prep():
    print("\n\nGraph 1")
    print("====================================================")
    # create graph
    graph = searchAlg(5, 4)
    # set parameters of graph to graph 1
    graph.setAgentLocation(2, 2)
    graph.setDirtyRooms([[1, 2], [2, 4], [3, 5]])
    # print out graph
    debugRooms(graph.rooms, graph.currLoc)
    # run search 1
    idt_search_run(graph)
    # set parameters of graph to graph 2
    graph.setRoomClean(3, 5)
    graph.setAgentLocation(3, 2)
    graph.setDirtyRooms([[1, 2], [2, 4], [2, 1], [3, 3]])
    # reset tracking variables used in graph
    graph.idsnodescreated = 0
    graph.idsnodesexpanded = 0
    graph.idssequence=[]
    graph.idscleanedit = 0
    graph.idsstart=[0,0]
    graph.idsfirstfive=[]
    graph.currScore = 0.0
    graph.visited = []
    # run search 2
    print("\n\nGraph 2")
    print("====================================================")
    debugRooms(graph.rooms, graph.currLoc)
    # print out graph
    idt_search_run(graph)


def idt_search_run(graph):
    # start timer
    start = timeit.default_timer()
    # reset graph score to 0
    graph.currScore = 0.0
    # Initiate IDDFS
    # create variables, update tracking variables in graph
    graph.idsstart = [graph.currLoc[0], graph.currLoc[1]]
    maxdepth = 0
    while True:
        idt_depth_search(graph, maxdepth)
        if graph.areAllRoomsClean():
            graph.idssequence.append("SUCK")
            break
        graph.setAgentLocation(graph.idsstart[0],graph.idsstart[1])
        if graph.idscleanedit ==1:
            graph.idssequence.append("SUCK")
            maxdepth =1
        else:
            maxdepth += 1
        graph.idscleanedit=0
        graph.visited = []
    # end timer
    end = timeit.default_timer()

    # print info
    #   first 5 search nodes in the order they would be expanded
    #   total number of nodes expanded
    #   the total number of nodes generated,
    #   the CPU execution time in seconds.
    print("\n====================================================")
    print("First five nodes visited: "+str(graph.idsfirstfive))
    print("====================================================")
    print("Nodes created: "+ str(graph.idsnodescreated))
    print("Nodes Expanded: "+str(graph.idsnodesexpanded))
    print("Time Elapsed: " +  str(end - start) + " seconds")
    #   The solution found
    print("====================================================")
    print("Solution Sequence: " + str(graph.idssequence))
    print("Number of moves: " + str(len(graph.idssequence)))
    print("Solution Cost: " + str(graph.currScore))
    print("====================================================")
    # reset the graph



def idt_depth_search(graph, depth):
    if graph.idscleanedit == 1:
        return
    # get current room
    room = graph.getCurrentRoom(graph.currLoc[0], graph.currLoc[1])
    if len(graph.idsfirstfive) < 5:
        graph.idsfirstfive.append([room.x,room.y])
    # increment nodes expanded
    graph.idsnodescreated += 1
    # add the current node to list of visited nodes
    graph.visited.append([room.x, room.y])
    # check if room is dirty
    if room.isDirty:
        # if room is dirty we set to clean and add to score
        room.isDirty = False
        graph.currScore += 5
        graph.idscleanedit = 1
        # set cleaned room as start of nect IDS sequence
        graph.idsstart =[room.x, room.y]
        return
    # used to make sure we don't go past the depth limit of this current IDS
    if depth == 0:
        return
    # create neighbor cords, all neighbors are rooms that are 1 action from current room
    neighborslist = [[room.x, room.y-1], [room.x-1, room.y],  [room.x, room.y + 1], [room.x + 1, room.y]]
    # iterate over all neighboring rooms
    for neighbor in neighborslist:
        # check that the room cords created are within the bounds of graph,
        # if it is outside upper limit or 0 remove it from list of neighbors
        if neighbor[0] > 4 or neighbor[1] > 5:
            neighborslist.remove([neighbor[0], neighbor[1]])
        elif neighbor[0] and neighbor[1] != 0:
            # increment nodes expanded
            graph.idsnodesexpanded += 1
            # check that the neighbor has not already been added before,
            # we are running a tree search on a undirected graph
            # it is necessary otherwise it can get stuck in cycles
            # bad coding practive, could move most into seperate function but im lazy
            if neighbor not in graph.visited:
                if neighbor[1] < room.y:
                    graph.offsetAgent(0, -1)
                    idt_depth_search(graph, (depth - 1))
                    if graph.idscleanedit ==1:
                        graph.currScore += 1
                        graph.idssequence.append("UP")
                        return
                    graph.offsetAgent(0, 1)
                elif neighbor[1] > room.y:
                    graph.offsetAgent(0, 1)
                    idt_depth_search(graph, (depth - 1))
                    if graph.idscleanedit ==1:
                        graph.currScore += 2
                        graph.idssequence.append("DOWN")
                        return
                    graph.offsetAgent(0, -1)
                elif neighbor[0] < room.x:
                    graph.offsetAgent(-1, 0)
                    idt_depth_search(graph, (depth - 1))
                    if graph.idscleanedit ==1:
                        graph.currScore += 3
                        graph.idssequence.append("LEFT")
                        return
                    graph.offsetAgent(1, 0)
                elif neighbor[0] > room.x:
                    graph.offsetAgent(1, 0)
                    idt_depth_search(graph, (depth - 1))
                    if graph.idscleanedit == 1:
                        graph.currScore += 4
                        graph.idssequence.append("RIGHT")
                        return
                    graph.offsetAgent(-1, 0)
        else:
            neighborslist.remove([neighbor[0], neighbor[1]])


idt_search_prep()
