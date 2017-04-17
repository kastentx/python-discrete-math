import numpy as np
from collections import Counter
# import sys
import itertools

# Load the adjacency matrix
G = np.loadtxt("graphs/graph2.txt", int)

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
# NOTES this is a bit weird... not sure if this if clause is reversed
# and I'm not sure if the i+1 is necessary.. its giving results
# that are too big
        if (notDominating == False):
            print(filtered[j], isDom(filtered[j], G, 'closed'))
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
#                print(filtered[j])
                return len(filtered[j])
#            print(filtered[j], independant)

def cliqueNumber(G):
    for i in reversed(range(1,order(G)+1)):
        filtered = [x for x in powerset(set(range(order(G)))) if len(x) == i]
        for j in range(len(filtered)):
            clique = True
            for n in filtered[j]:
                for m in filtered[j]:
                    if G[n][m] != 1 and n != m:
                        clique = False
            if (clique):
#                print(filtered[j])
                return len(filtered[j])
#            print(filtered[j], clique)

def distance(G, v1, v2):
    distance = 0
    if v1 == v2:
        return distance
    visited = openNeighborhood(G, v1)
    distance += 1
    while v2 not in visited and distance < order(G):
        for v in visited.copy():
            visited = visited | closedNeighborhood(G, v)
        distance += 1
    if v2 in visited:
        return distance
    else:
        return -1
#        return 'not connected'

def eccentricity(G, v):
#    print([distance(G, v, v2) for v2 in range(order(G)) if v != v2])
    return np.amax([distance(G, v, v2) for v2 in range(order(G)) if v != v2])

def radius(G):
    return np.amin([eccentricity(G, x) for x in range(order(G))])

def diameter(G):
    return np.amax([eccentricity(G, x) for x in range(order(G))])

def cycle(G, v):
    length = 0
    neighbors = closedNeighborhood(G, v)
#    print('neighbors', neighbors)
    length += 1
    while v not in neighbors and length <= order(G):
        oldNeighbors = neighbors.copy()
        for x in neighbors.copy():
            neighbors = neighbors | closedNeighborhood(G, x)
        neighbors = neighbors - oldNeighbors 
        if (length == 1):
            neighbors = neighbors - {v}
#        print('adding one to length...', neighbors)
        length += 1
    if v in neighbors:
        return length
    else:
        # changing error output to 0 instead of a string
        return 0

def girth(G):
    return np.amax([cycle(G, x) for x in range(order(G))])

def residue(G):
    dSeq = degreeSequence(G)
#    print(dSeq)
    maxD = dSeq[0]
    while maxD > 0:
        dSeq.remove(dSeq[0])
        for i in range(maxD):
            dSeq[i] -= 1
        dSeq.sort(reverse = True)
#        print(dSeq)
        maxD = dSeq[0]
    residue = len(dSeq)
    return residue

def chromatic(G):
    vertices = list(range(order(G)))
    colorList = list(range(maxDegree(G) + 1))
    coloring = [-1] * order(G)
#    print(coloring)
#    print(vertices)
#    print(colorList)
    for i in range(order(G)):
        neighbors = closedNeighborhood(G, i)
        neighborColors = set()
        for j in neighbors:
            neighborColors.add(coloring[j])
        print('neighbors of %d' % i, neighbors)
#        print(coloring)
        for c in colorList:
            print('neighbor colors of %d' % i, neighborColors)
            if c not in neighborColors:
                print('\tassigning color {0} to vertex {1}'.format(c,i))
                coloring[i] = c
                break
    coloring = [x for x in coloring if x != -1]
    # Counter.keys() gives us unique colors used (no repeats)
    # the len() method counts num of colors used
    return len(set(coloring))
#    return len(Counter(coloring).keys())


    # NEW NOTES
    # a graph with size 0 is the only graph with X(G) = 1
    # a bipartite graph with at least one edge has X(G) = 2
    # an odd-cycle has X(G) = 3


    # if graph is complete, then maxDegree+1 colors are needed
    # otherwise, chromatic number is at most maxDegree
    # but it is greater than/equal to the clique number

    # this means that at least we can restrict the range
    # even if the algorithm itself is super slow

def complement(G):
    complement = G.copy()
    for i in range(order(G)):
        for j in range(order(G)):
            if G[i][j] == 0 and i != j:
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
print('clique number:', cliqueNumber(G))
print('distance between 2 and 0:', distance(G, 2, 0))
print('eccentricity of v2:', eccentricity(G, 2))
print('radius of G:', radius(G))
print('diameter of G:', diameter(G))
print('residue of G:', residue(G))
# print('length of cycle for v2:', cycle(G, 2))
print('girth of G:', girth(G))
print('chromatic:', chromatic(G))
#print('complement:\n', complement(G))
#print('\n')
#for i in range(0,order(G)):
#    print('degree of %s:' % i, degree(G,i))
#    print('open neighborhood of %s:' % i, openNeighborhood(G,i))
#    print('closed neighborhood of %s:' % i, closedNeighborhood(G,i))
