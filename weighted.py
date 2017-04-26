import numpy as np

# sort the edges

# utility functions
def weight(edge):
    return edge[2]

def nodes(edge):
    return [edge[0],edge[1]]
    
def nodesInG(G):
    V = set()
    for edge in G:
        V.add(edge[0])
        V.add(edge[1])
    return V

def displayEdges(G):
    for edge in G:
        print('nodes: {0}'.format(nodes(edge)))
        print('weight: {0}\n'.format(weight(edge)))

def getSortedEdges(G):
    return sorted(G, key=weight)



G = np.loadtxt('graphs/weighted1.txt', int)
V = nodesInG(G)

# FUNCTION CALLS
print(G, '\n')


print('nodes: {0}'.format(V))
displayEdges(G)
print('edges sorted by weight: {0}'.format(getSortedEdges(G)))
