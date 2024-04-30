class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class DoublyList:
    def __init__(self):
        self.head = None

    def inertintolist(self,data):
        if self.head == None:
            t = Node(data)

            t.prev=self.head
            self.head=t
        else:
            temp=self.head
            t=Node(data)
            temp.next=t
            t.prev=temp
            self.head=t

    def insertAt(self,i,data):
        if i == 0:
            t=self.head
            while(t.prev):
                t=t.prev
            k = Node(data)
            k.next=t
            self.head=k
        else:
            k=0
            t= self.head
            while t.prev:
                if k == i:
                    temp=t.prev
                    temp2 = Node(data)
                    t.prev= temp2
                    temp2.next=t
                    temp2.prev=temp
                t=t.prev
                k=k+1




    def printDl(self):
        r = self.head
        while(r):
            print(r.data)
            r=r.prev


dl = DoublyList()
dl.inertintolist(5)
dl.inertintolist(4)
dl.inertintolist(0)
print
dl.insertAt(1,'kkkk')
dl.printDl()

