import numpy as np
import collections
import sys
import itertools

# Load the adjacency matrix
G = np.loadtxt("Paw.txt", int)
print("The adjacency matrix of G is: ")
print(G)


def order(G):
    n = len(G)
    return n

def openNeighborhood(G,v):
    neighborhood = set()
    for i in range(0,order(G)):
        if G[v][i] == 1:
            neighborhood.add(i)
    return neighborhood

def degree(G,v):
    d = len(openNeighborhood(G,v))
    return d

# Function Calls
print(openNeighborhood(G,1))
print(degree(G,1))
