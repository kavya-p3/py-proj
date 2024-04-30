class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight



class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex




    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:

            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)




g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(1, 5, 300)
g.addEdge(0, 1, 100)


g.addEdge(0, 3, 99)
print(g.vertList)
