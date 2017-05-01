import numpy as np

class WeightedGraph:
    edges = []
    vertices = []
    myGraphArray = []
    def __init__(self, graphArray):
        self.edges += [[[x[0],x[1]], x[2]] for x in graphArray]
        self.vertices += [[x] for x in range(len(graphArray)-1)]
        self.myGraphArray = graphArray

    def __weight(self, edge):
        return edge[1]

    def __sortedEdges(self):
        return sorted(self.edges, key=self.__weight)

    def __find(self, vertex):
        for parent in range(len(self.vertices)):
            for child in self.vertices[parent]:
                if child == vertex:
                    return parent
        return None

    def __union(self, V, a, b):
        rootA = self.__find(a)
        rootB = self.__find(b)
        for vertex in V[rootB]:
            V[rootA].append(vertex)
        V.pop(rootB)

    def kruskals(self):
        E = self.__sortedEdges()
        V = self.vertices 
        MST = set()
        i = 0
        # when the length of V equals 1, we will know the subgraph is connected
        while len(V) > 1:
            if self.__find(E[i][0][0]) != self.__find(E[i][0][1]):
                MST.add((E[i][0][0],E[i][0][1]))
                self.__union(V, E[i][0][0], E[i][0][1])
            i += 1
        # NOTE this resets the vertices array back to idividual nodes
        self.vertices.pop()
        self.vertices += [[x] for x in range(len(self.myGraphArray)-1)]
        return MST

    def prims(self):
        E = self.edges
        V = self.vertices
        costIndex = []
        for v in range(len(self.vertices)-1):
            if E[v][0][0] == v or E[v][0][1] == v:
                print('edge found: {0} weight: {1}'.format(E[v],E[v][1]))
            tree = set()
        return costIndex
