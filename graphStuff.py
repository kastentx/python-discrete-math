import numpy as np
import collections
import sys
import itertools

# Load the adjacency matrix
G = np.loadtxt("graphs/graph7.txt", int)

def order(G):
    return len(G)

def size(G):
    return int(np.sum(G) / 2)

def degree(G,v):
    return np.sum(G[v])

def maxDegree(G):
    return np.amax(np.sum(G, axis=1))

def minDegree(G):
    return np.amin(np.sum(G, axis=1))

def degreeSequence(G):
    return sorted(np.sum(G, axis=1), reverse=True)

def openNeighborhood(G,v):
    neighborhood = set()
    for i in range(order(G)):
        if G[v][i] == 1:
            neighborhood.add(i)
        neighborhood.add(v)
    return neighborhood

def closedNeighborhood(G,v):
    closed = openNeighborhood(G,v).copy()
    closed.discard(v)
    return closed

def isConnected(G):
    totalNeighbors  = openNeighborhood(G,0)
    for i in range(1,order(G)):
        for j in totalNeighbors:
            newNeighbors = openNeighborhood(G,j) - totalNeighbors
            if len(newNeighbors) > 0:
                break
        totalNeighbors = totalNeighbors | newNeighbors 
        if len(totalNeighbors) == order(G):
            break
    return True if len(totalNeighbors) == order(G) else False

def isDom(S, G):
    totalNeighbors = set()
    for v in S:
        totalNeighbors = totalNeighbors | openNeighborhood(G,v)
    #print(totalNeighbors)
    return (len(totalNeighbors) == order(G))


def complement(G):
    complement = G
    for i in range(order(G)):
        for j in range(order(G)):
            if G[i][j] == 0:
                complement[i][j] = 1
            else:
                complement[i][j] = 0
    return complement


# Function Calls
print("The adjacency matrix of G is: ")
print(G)
print('\n')
print('order of G:', order(G))
print('size:', size(G))
print('max degree:', maxDegree(G))
print('min degree:', minDegree(G))
print('degree sequence:', degreeSequence(G))
print('connected:', isConnected(G))
S = {2, 4}
print('2 and 4 dominate?', isDom(S,G))
print('complement:\n', complement(G))
print('\n')
for i in range(0,order(G)):
    print('degree of %s:' % i, degree(G,i))
    print('open neighborhood of %s:' % i, openNeighborhood(G,i))
    print('closed neighborhood of %s:' % i, closedNeighborhood(G,i))
