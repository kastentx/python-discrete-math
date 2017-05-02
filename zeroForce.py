import numpy as np
import graphStuff as gs
G = np.loadtxt("graphs/dodecahedron.txt", int)

def zeroForceNum(G):
    vertices = list(range(gs.order(G)))
    allCombos = gs.powerset(set(range(gs.order(G))))
    targetNode = None 

    for combo in allCombos:
        size = len(combo)
        toColor = {0}
        iterCount = 0
        coloring = [0] * gs.order(G)
        for v in combo:
            coloring[v] = 1
        print('\npotential zero-forcing set',combo)
        # NOTE here is where we look at each starting thing
        while len(toColor):
            iterCount += 1
            toColor = set()
            for n in vertices:
                noColorNeighborCount = 0
#                print('checking {0}'.format(n))
                neighbors = gs.closedNeighborhood(G, n)
                for m in neighbors:
                    if coloring[m] == 0:
                        targetNode = m
#                        print('target: {0}'.format(targetNode))
#                        print('I need to color {0}'.format(targetNode))
                        noColorNeighborCount += 1
                if noColorNeighborCount == 1 and coloring[n] == 1:
#                    print('coloring {0}s one non-color neighbor {1}'.format(n ,targetNode))
                    toColor.add(targetNode)
            if len(toColor): 
                print('{0} should be colored for next iteration'.format(toColor))
                # color the set of target nodes
                for n in toColor:
                    coloring[n] = 1
                print('new coloring: {0}'.format(coloring))
                if np.sum(coloring) == gs.order(G):
                    print('\nthis set is colored now after {0} iterations'.format(iterCount))
                    print('zero forcing set',combo)
                    return size

def subTotalDom(G):
    mySum = 0
    index = 0
    for d in gs.degreeSequence(G):
        index += 1
#        print(index, d)
        mySum += d
        if mySum >= gs.order(G):
            return index 

def annihilationNum(G):
    mySum = 0
    index = 0
    for d in sorted(gs.degreeSequence(G)):
#        print(index, d)
        mySum += d
        if mySum > gs.size(G):
            return index
        index += 1

def avgDegree(G):
    return int(np.sum(gs.degreeSequence(G)) / gs.order(G))

# print(avgDegree(G))
# print(annihilationNum(G))
# print(subTotalDom(G))
print('zero forcing number for G is',zeroForceNum(G))
