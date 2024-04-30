class Graph:
    def __init__(self):
        self.adjList = {}
        # for i in self.nodes:
        #     self.adjList[i] = []

    def insertEdge(self, src, dest):
        if src not in self.adjList.keys():
            self.adjList[src] = []
        self.adjList[src].append(dest)

    def degreeofNode(self, n):
        return len(self.adjList[n])

    def printEdgesOfVertex(self, v):
        # for i in self.adjList[v]:
        print(v, '--->', [i for i in self.adjList[v]])

    def DFS(self,start):
        dist={}
        visited =  set()
        stack = [start]
        dist[start]=0
        visited.add(start)
        while stack:
            for i in self.adjList[stack[0]]:
                if i is not visited:
                    visited.add(i)




g = Graph()

g.insertEdge('a','b')
g.insertEdge('a','c')
g.insertEdge('b','d')
g.insertEdge('c','d')
g.insertEdge('c','e')
g.insertEdge('d','e')
print(g.adjList)