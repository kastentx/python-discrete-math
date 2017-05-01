import numpy as np
import book_of_four as bf

G = np.loadtxt('graphs/weighted2.txt', int)

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
    return [(x[0], x[1], x[2]) for x in sorted(G, key=weight)]

def realKruskals(G):
    forest = [bf.Node(x) for x in nodesInG(G)]
    visitedNodes = set()
    visitedEdges = set()
    [bf.makeSet(x) for x in forest]
    edgeList = [x for x in sortedEdges(G)]
    for edge in edgeList:
        if bf.find(nodes(edge)[0]) == bf.find(nodes(edge)[1]):
            print('found {0} and {1} in the same tree.'.format(nodes(edge)[0],nodes(edge)[1]))
    


def kruskals(G):
    visited = set()
    visitedNodes = {x for x in visited}
    visited.add((G[0][0], G[0][1], G[0][2]))
    edgeList =[x for x in sortedEdges(G)]
    for edge in sortedEdges(G):
        if nodes(edge)[0] not in visitedNodes or nodes(edge)[1] not in visitedNodes:
            visited.add(edge)
            visitedNodes = visitedNodes | {x for x in nodes(edge)}
#            print('this is the edge var:', edge)
            edgeList.remove(edge)
            # NOTE if the node isn't connected.. here is where we should detect
            # that and make it connect
    if len(visited) < len(G) - 1:
        print('visited edges:', visited)
        print('visited nodes:', visitedNodes)
        print('remaining edges:', edgeList)
    return visited
# NOTE once the inital scan is done, make another pass adding until the lowest
# possible num of edges is reached for a connected graph with n vertices



# FUNCTION CALLS
print(G, '\n')

displayEdges(G)
print('\nkruskals {0}'.format(realKruskals(G)))
# print('edges sorted by weight: {0}'.format(sortedEdges(G)))
