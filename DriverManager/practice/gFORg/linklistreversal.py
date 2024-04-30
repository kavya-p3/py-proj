class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
       self.head = None

    def insertintolistatfront(self,data):
        for i in data:
          n = Node(i,self.head)
          self.head = n

    def printlinkedlist(self):
        itr = self.head
        while (itr):
            print(itr.data,'--->',end='')
            itr = itr.next

    def reversell(self):
        current=self.head
        prevN=None
        nextN=None
        while(current):
            nextN=current.next
            current.next=prevN
            prevN=current
            current=nextN

        self.head=prevN

    def reverseRecurssion(self,current,prev,next):
        if (current):
            next = current.next
            current.next = prev
            prev = current
            current = next
            self.reverseRecurssion(current,prev,next)
        self.head = prev


    def kthelementlongway(self,n):
        left=self.head
        right=self.head
        for i in range(n-1):
            right=right.next

        while(right.next):
            left=left.next
            right=right.next
        print(left.data)









l = Linkedlist()
li = ['mango','orange','pineapple','citaphal','raspberry']
l.insertintolistatfront(li)
l.printlinkedlist()
print()
#l.reversell()
#l.printlinkedlist()
#l.reverseRecurssion(l.head,None,None)
#l.printlinkedlist()
l.kthelementlongway(1)