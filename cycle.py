import numpy as np

G = np.loadtxt("graphs/graph10.txt", int)

def order(G):
    return len(G)

def degree(G, v):
    return np.sum(G[v])

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

def closedNeighborhood(G, v):
    neighborhood = set()
    for i in range(order(G)):
        if G[v][i] == 1:
            neighborhood.add(i)
#    print (neighborhood)
    return neighborhood

def find_all_paths(G, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    neighbors = [x for x in closedNeighborhood(G,start)]
    for n in neighbors:
        if n not in path:
            newpaths = find_all_paths(G, n, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return sorted(paths, key=len)

def find_path(G, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    neighbors = [x for x in closedNeighborhood(G,start)]
    for n in neighbors:
        if n not in path:
            newpath = find_path(G, n, end, path)
            if newpath:
                return newpath
    return None

def find_cycle(G, v):
    neighbors = [x for x in closedNeighborhood(G, v) if degree(G, x) > 1]
    length = 0
    for n in neighbors:
        paths = find_all_paths(G, v, n)
        length = len(paths[1])
        if (length > 2):
            return length
        else:
            return 0

def eccentricity(G, v):
    # loop through all vertices and find longest path to the one passed as arg
    # save the longest one of all these and thats your answer
    maxLength = 0
    for x in range(order(G)):
        if (x != v):
#            print(find_all_paths(G, v, x))
             pathLengths = sorted([len(x) for x in find_all_paths(G, v, x)],
                     reverse=True)
#            if np.amax(pathLengths) > maxLength:
#                maxLength = np.amax(find_all_paths(G, v, x))
#    return maxLength
    return pathLengths[0] - 1


print(find_cycle(G, 3))
print(eccentricity(G, 0))
