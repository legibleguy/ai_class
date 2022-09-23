from GraphBase import searchAlg
from RoomsBase import debugRooms
# used during testing in order to create graphs for search to test
# in final version idt_search_run can just be passed a graph directly
def idt_search_prep():
    # create fringe
    # create graph1
    graph = searchAlg(5, 4)
    graph.setAgentLocation(2, 2)
    graph.setDirtyRooms([[1, 2], [2, 4], [3, 5]])
    debugRooms(graph.rooms, graph.currLoc)
    # run search 1
    idt_search_run(graph)
    # change graph to second parameters
    graph.setRoomClean(3, 5)
    graph.setAgentLocation(3, 2)
    graph.setDirtyRooms([[2, 1], [3, 3]])
    debugRooms(graph.rooms, graph.currLoc)
    # run search on updated graph


def idt_search_run(graph,fringe,):
    # start timer
    # determine start position
    # run
    # end timer
    # print info


idt_search_prep()