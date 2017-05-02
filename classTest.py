import numpy as np
import book_of_four as bf

G = np.loadtxt('graphs/weighted2.txt', int)

myGraph = bf.WeightedGraph(G)

print(myGraph.myGraphArray)
#print('kruskal MST:', myGraph.kruskals())
print(myGraph.prims())
