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

    def __minCostEdge(self, v):
        cost = 1000
        edge = []
        for e in self.edges:
            if e[0][0] == v or e[0][1] == v:
                if self.__weight(e) < cost:
                    cost = self.__weight(e)
                    edge = e
        return edge

    def __incidentEdges(self, v):
        edges = []
        for e in self.edges:
            if e[0][0] == v or e[0][1] == v:
                edges.append(e)
        return edges

    def __nodesInE(self, e):
        return [e[0][0],e[0][1]]
    def kruskals(self):
        E = self.__sortedEdges()
        V = self.vertices 
        MST = list()
        i = 0
        # when the length of V equals 1, we will know the subgraph is connected
        while len(V) > 1:
            if self.__find(E[i][0][0]) != self.__find(E[i][0][1]):
                MST.append([[E[i][0][0],E[i][0][1]], E[i][1]])
                self.__union(V, E[i][0][0], E[i][0][1])
            i += 1
        # NOTE this resets the vertices array back to idividual nodes
        self.vertices.pop()
        self.vertices += [[x] for x in range(len(self.myGraphArray)-1)]
        return MST

    def prims(self):
        vTree = []
        vKeys = dict()
        MST = dict()
        # initialize nodes
        for v in range(len(self.vertices)):
            vKeys.update({v:999})
        vKeys.update({0:0})


        while len(vTree) != len(self.vertices):
            lowestKey = 1000
            lowNode = -1
            for n in vKeys:
                if vKeys[n] < lowestKey and n not in vTree:
                    lowestKey = vKeys[n]
                    lowNode = n
            vTree.append(lowNode)
            # finding adjacent nodes
            adjacentNodes = []
            for edge in self.__incidentEdges(lowNode):
                edgeNodes = self.__nodesInE(edge)
                for i in edgeNodes:
                    if i not in vTree:
                        adjacentNodes.append(i)
            # updating scores of adjacent nodes
            for k in adjacentNodes:
                for e in self.edges:
                    if k in self.__nodesInE(e) and lowNode in self.__nodesInE(e):
                        if self.__weight(e) < vKeys[k]:
                            vKeys[k] = self.__weight(e)
                            MST[k] = e
        return list(MST.values())
