#showcasing the Uniform Cost Graph search
from GraphBase import graph
from GraphBase import debugGraph
import time
from UniformCost import UniformCostSearch
import sys #this is just to log the prints into a file
old_stdout = sys.stdout
log_file = open("reports_uniformcostgraph.log","w")
sys.stdout = log_file

#Instance #1: Initial agent location: (2,2). Dirty squares: (1,2), (2,4), (3,5).
firsFive = []
created = []
created.append(0)
expanded = []
expanded.append(0)
mygraph = graph(4, 5)
mygraph.setDirtyRooms([[1,2], [2,4], [3,5]])
startTime = time.time()
path = UniformCostSearch(mygraph, [2, 2], False, firsFive, created, expanded)

print("Graph 1. Initial agent location: (2,2). Dirty squares: (1,2), (2,4), (3,5).")
print("====================================================")
debugGraph(mygraph, [2,2])
print("====================================================")
print("First five nodes visited + graph representation: ")
for n in firsFive:
    print(n)
    debugGraph(n.state, n.location)
    print("-------------------------------------")

print("====================================================")
print("Nodes created: " + str(created[0]))
print("Nodes expanded: " + str(expanded[0]))
print("Time elapsed: " + str(time.time() - startTime) + " seconds")
print("Solution cost: " + str(path.cost))
print("Final path: " + path.getPath())
print("Actions list: " + path.getMoves())
print("Number of moves: " + str(path.getTotalNumNodes()))

##
print("\n")
print("\n")

#Instance #2: Initial agent location: (3,2). Dirty squares: (1,2), (2,1), (2,4), (3,3). 
firsFive = []
created = []
created.append(0)
expanded = []
expanded.append(0)
mygraph = graph(4, 5)
mygraph.setDirtyRooms([[1,2], [2,1], [2,4], [3,3]])
startTime = time.time()
path = UniformCostSearch(mygraph, [3, 2], False, firsFive, created, expanded)

print("Graph 2. Initial agent location: (3,2). Dirty squares: (1,2), (2,1), (2,4), (3,3).")
print("====================================================")
debugGraph(mygraph, [3,2])
print("====================================================")
print("First five nodes visited + graph representation: ")
for n in firsFive:
    print(n)
    debugGraph(n.state, n.location)
    print("-------------------------------------")

print("====================================================")
print("Nodes created: " + str(created[0]))
print("Nodes expanded: " + str(expanded[0]))
print("Time elapsed: " + str(time.time() - startTime) + " seconds")
print("Solution cost: " + str(path.cost))
print("Final path: " + path.getPath())
print("Actions list: " + path.getMoves())
print("Number of moves: " + str(path.getTotalNumNodes()))

sys.stdout = old_stdout
log_file.close()