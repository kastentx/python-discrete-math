import numpy as np
import collections
import sys
import itertools

# Load the adjacency matrix
G = np.loadtxt("graphs/graph3.txt", int)

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

def openNeighborhood(G,v):
    neighborhood = set()
    for i in range(0,order(G)):
        if G[v][i] == 1:
            neighborhood.add(i)
    return neighborhood



# Function Calls
print("The adjacency matrix of G is: ")
print(G)
print('\n')
print('order of G:', order(G))
print('size:', size(G))
print('max degree:', maxDegree(G))
print('min degree:', minDegree(G))
print('\n')
for i in range(0,order(G)):
    print('degree of %s:' % i, degree(G,i))
    print('open neighborhood of %s:' % i, openNeighborhood(G,i))
