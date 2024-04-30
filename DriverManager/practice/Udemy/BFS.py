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
                d[bucket] += [word]
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    # print(d)
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.insertEdge(word1, word2)

    return g


def bfsandpath(g, start, stop):
    if stop not in g.adjList.keys() or start not in g.adjList.keys():
        print('there can never be a path')
        return

    visited = set()
    dist = {}
    dist[start] = 0
    dist[stop] = 0
    q = [start]
    visited.add(start)
    
    while q:
        vertex = q.pop(0)
        for i in g.adjList[vertex]:
            if i not in visited:
                visited.add(i)
                q.append(i)
                dist[i] = dist[vertex] + 1

    print(dist)


# li = ['a','b','c','d','e']
# g = Graph(li)
#
# g.insertEdge('a','b',9)
# g.insertEdge('a','c',4)
# g.insertEdge('b','d',5)
# g.insertEdge('c','d',6)
# g.insertEdge('c','e',3)
# g.insertEdge('d','e',2)
# print(g.adjList)
# print(g.degreeofNode('c'))
# g.printEdgesOfVertex('c')
g = readFromFile('C:\\Users\\kp\\Documents\\wordFile.txt')
bfsandpath(g,'POOL','SAGE')
# for v in g.adjList.keys():
#     g.printEdgesOfVertex(v)

bfsandpath(g, 'ZZZZ', 'POLL')
