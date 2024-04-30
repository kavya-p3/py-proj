class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        #return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
        return str([x.id for x in self.connectedTo])


    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


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

    def __iter__(self):
        return iter(self.vertList.values())


def readFromFile(wordFile):
    d = {}
    g = Graph()

    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        print
        line
        word = line[:-1]
        print
        word
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d.keys():
                d[bucket]+=[word]
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    #print(d)
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)

    return g

def bfsshortestpath(g,start, goal):

        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                t =g.vertList[vertex]
                print(t)
                queue.extend(t - visited)
        return visited



g = readFromFile('C:\\Users\\kp\\Documents\\wordFile.txt')
print('------------------------------>')
print(g.numVertices)
print(g.vertList)

for vertex in g.vertList.values():
    print (vertex)
    #print (vertex.getConnections())

print(bfsshortestpath(g,'POOL','SAGE'))
v = g['POOL']
print(v)


