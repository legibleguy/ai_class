from GraphBase import searchAlg
from RoomsBase import debugRooms
from RoomsBase import Room
from RoomsBase import Action
from RoomsBase import actionCost
from RoomsBase import actionDir
import time


# used during testing in order to create graphs for search to test
# in final version idt_search_run can just be passed a graph directly
def idt_search_prep():
    # create fringe
    fringe = []
    # create graph1
    graph = searchAlg(5, 4)
    graph.setAgentLocation(2, 2)
    graph.setDirtyRooms([[1, 2], [2, 4], [3, 5]])
    debugRooms(graph.rooms, graph.currLoc)
    # run search 1
    idt_search_run(graph, fringe)
    # change graph to second parameters
    graph.setRoomClean(3, 5)
    graph.setAgentLocation(3, 2)
    graph.setDirtyRooms([[2, 1], [3, 3]])
    debugRooms(graph.rooms, graph.currLoc)
    # run search on updated graph


def idt_search_run(graph, fringe):
    # start timer
    start = time.time()
    # reset graph score to 0
    graph.currScore = 0.0
    # Initat IDDFS
    maxdepth = 0
    nodescreated = 0
    rootx, rooty = graph.currLoc
    # i=0
    while not graph.areAllRoomsClean():
        idt_depth_search(graph, maxdepth, fringe, nodescreated)
        nodescreated += 1
        maxdepth += 1
        graph.setAgentLocation(rootx, rooty)
        graph.visited = []
        # i+=1

    # end timer
    end = time.time()
    # reset the graph
    graph.currScore = 0.0
    graph.visited = []
    # print info
    #   first 5 search nodes in the order they would be expanded
    #   total number of nodes expanded
    #   the total number of nodes generated,
    #   the CPU execution time in seconds.
    print("Time Elapsed: " +  str(end - start))
    #   The solution found


def idt_depth_search(graph, depth, fringe, nodescreated):

    print("cum  " + str(nodescreated) + "   " + str(depth))
    print("current room is: (" + str(graph.currLoc[0])+","+str(graph.currLoc[1])+")")
    # get current room
    room = graph.getCurrentRoom(graph.currLoc[0], graph.currLoc[1])
    # check if room is dirty
    graph.visited.append([room.x, room.y])
    if room.isDirty:
        print('cleaned a room: (" + str(graph.currLoc[0])+","+str(graph.currLoc[1])+")"')
        room.isDirty = False
        graph.currScore += 5
        # check if all rooms are cleaned, if so then exit everything
        if graph.areAllRoomsClean():
            return 1

    if depth == 0:
        return
    # for neighbor in graph.neighbors:
    #     # print(neighbor)
    #     nodescreated += 1
    #     if idt_depth_search(neighbor, depth-1, fringe, nodescreated):
    #         return True

    # create neighbor cords
    neighborslist = [[room.x, room.y - 1], [room.x - 1, room.y], [room.x + 1, room.y], [room.x, room.y + 1]]
    print(neighborslist)
    for neighbor in neighborslist:
        if neighbor[0] > 4 or neighbor[1] > 5:
            print(":do we enter here>")
            neighborslist.remove([neighbor[0], neighbor[1]])
        elif neighbor[0] and neighbor[1] != 0:
            print("do we enter herez")
            if neighbor not in graph.visited:
                if neighbor[1] < room.y:
                    print("do we enter here1")
                    nodescreated += 1
                    graph.offsetAgent(0, -1)
                    graph.currScore += 1
                    idt_depth_search(graph, (depth - 1), fringe, nodescreated)
                    graph.offsetAgent(0, 1)
                if neighbor[0] < room.x:
                    print("do we enter here2")
                    nodescreated += 1
                    graph.offsetAgent(-1, 0)
                    graph.currScore += 3
                    idt_depth_search(graph, (depth - 1), fringe, nodescreated)
                    graph.offsetAgent(1, 0)
                if neighbor[0] > room.x:
                    print("do we enter here3")
                    nodescreated += 1
                    graph.offsetAgent(1, 0)
                    graph.currScore += 4
                    idt_depth_search(graph, (depth - 1), fringe, nodescreated)
                    graph.offsetAgent(-1, 0)
                if neighbor[1] > room.y:
                    print("do we enter here4")
                    nodescreated += 1
                    graph.offsetAgent(0, 1)
                    graph.currScore += 2
                    idt_depth_search(graph, (depth - 1), fringe, nodescreated)
                    graph.offsetAgent(0, -1)
        else:
            print(":do we enter here0")
            neighborslist.remove([neighbor[0], neighbor[1]])

    # if graph.rooms[graph.currLoc].isDirty is True:
    #     graph.setRoomClean(graph.rooms[graph.currLoc])
    #     graph.doAction(Action.SUCK)


idt_search_prep()
