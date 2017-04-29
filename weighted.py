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

def sortedEdges(G):
    return [x for x in sorted(G, key=weight)]



G = np.loadtxt('graphs/weighted1.txt', int)
V = nodesInG(G)

def kruskals(G):
    visited = set()
    visitedNodes = {x for x in visited}
    visited.add((G[0][0],G[0][1]))
    for edge in sortedEdges(G):
        if nodes(edge)[0] not in visitedNodes and nodes(edge)[1] not in visitedNodes:
            visited.add((nodes(edge)[0],nodes(edge)[1]))
            visitedNodes = visitedNodes | {x for x in nodes(edge)}
    return visited




# FUNCTION CALLS
print(G, '\n')


print('nodes: {0}'.format(V))
displayEdges(G)
print('\nkruskals {0}'.format(kruskals(G)))
# print('edges sorted by weight: {0}'.format(sortedEdges(G)))
