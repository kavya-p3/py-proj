class BinHeap:
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0


    def insert(self,k):
        self.heapList.append(k)
        self.currentSize+=1
        self.percUp(self.currentSize)

    def percUp(self,i):
         while i//2>0:
          if self.heapList[i]<self.heapList[i//2]:
            self.heapList[i//2],self.heapList[i]=self.heapList[i],self.heapList[i//2]
          i=i//2

    def printList(self):
        print(self.heapList)


    def delMin(self):
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize-=1
        self.heapList.pop()
        self.percDown(1)

    def minNode(self,i):
        if  i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def percDown(self,i):

        while i*2<=self.currentSize:
            print(i)
            mc = self.minNode(i)
            #print(mc)
            if self.heapList[mc]<self.heapList[i]:
                self.heapList[mc],self.heapList[i]=self.heapList[i],self.heapList[mc]
            i=mc

    def makeHeap(self,li):
          i=len(li)//2
          self.heapList = [0]+li[:]
          self.currentSize=len(li)
          #self.percUp(self.currentSize)
          while i>0:
              self.percDown(i)
              i=i-1


r=BinHeap()
# r.insert(10)
# r.insert(9)
# r.insert(12)
# r.insert(0)
# r.insert(6)
# r.insert(4)
# r.insert(9)
# r.insert(12)
# r.printList()
# r.delMin()
# r.printList()
li=[5, 7, 9, 1, 3]
r.makeHeap(li)
r.printList()
