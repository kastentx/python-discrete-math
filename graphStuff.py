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

def openNeighborhood(G, v):
    neighborhood = set()
    for i in range(order(G)):
        if G[v][i] == 1:
            neighborhood.add(i)
    neighborhood.add(v)
    return neighborhood

def closedNeighborhood(G, v):
    closed = openNeighborhood(G, v).copy()
    closed.discard(v)
    return closed

def isConnected(G):
    totalNeighbors  = openNeighborhood(G, 0)
    for i in range(1,order(G)):
        for j in totalNeighbors:
            newNeighbors = openNeighborhood(G, j) - totalNeighbors
            if len(newNeighbors) > 0:
                break
        totalNeighbors = totalNeighbors | newNeighbors 
        if len(totalNeighbors) == order(G):
            break
    return True if len(totalNeighbors) == order(G) else False

def powerset(iterable):
    s = list(iterable)
    return list(itertools.chain.from_iterable(itertools.combinations(s, r) for r in
        range(len(s) + 1)))

def totalDomNumber(G):
    for i in reversed(range(1,order(G)+1)):
        notDominating = True
        filtered = [x for x in powerset(set(range(order(G)))) if len(x) == i]
        for j in range(len(filtered)):
            if (isDom(filtered[j], G, 'closed')):
#                print(filtered[j], isDom(filtered[j],G))
                notDominating = False
#            else:
#                print(filtered[j], isDom(filtered[j],G))
        if (notDominating):
#            print(filtered[j], isDom(filtered[j],G))
            return i+1
    return 1

def domNumber(G):
    for i in reversed(range(1,order(G)+1)):
        notDominating = True
        filtered = [x for x in powerset(set(range(order(G)))) if len(x) == i]
        for j in range(len(filtered)):
            if (isDom(filtered[j], G)):
#                print(filtered[j], isDom(filtered[j],G))
                notDominating = False
#            else:
#                print(filtered[j], isDom(filtered[j],G))
        if (notDominating):
#            print(filtered[j], isDom(filtered[j],G))
            return i+1
    return 1

def isDom(S, G, neighbors = 'open'):
    totalNeighbors = set()
    for v in S:
        if (neighbors == 'open'):
            totalNeighbors = totalNeighbors | openNeighborhood(G,v)
        else:
            totalNeighbors = totalNeighbors | closedNeighborhood(G,v)
#        if (len(totalNeighbors) == order(G)):
#            print('neighbors of', S, totalNeighbors)
    return (len(totalNeighbors) == order(G))

def indyNumber(G):
    for i in reversed(range(1,order(G)+1)):
        filtered = [x for x in powerset(set(range(order(G)))) if len(x) == i]
        for j in range(len(filtered)):
            independant = True
            for n in filtered[j]:
                for m in filtered[j]:
                    if  G[n][m] == 1:
                        independant = False
            if (independant):
                return len(filtered[j])
#            print(filtered[j], independant)

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
#S = {2, 4}
#print('2 and 4 dominate?', isDom(S,G))
print('domination number:', domNumber(G))
print('total domination number:', totalDomNumber(G))
print('independance number:', indyNumber(G))
print('complement:\n', complement(G))
print('\n')
for i in range(0,order(G)):
    print('degree of %s:' % i, degree(G,i))
    print('open neighborhood of %s:' % i, openNeighborhood(G,i))
    print('closed neighborhood of %s:' % i, closedNeighborhood(G,i))
