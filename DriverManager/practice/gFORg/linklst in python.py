class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
       self.head = None

    def insertintolistatfront(self,data):
        n = Node(data,self.head)
        self.head = n

    def printlinkedlist(self):
        itr = self.head
        while (itr):
            print(itr.data,'--->',end='')
            itr = itr.next

    def insertintolistback(self,data):
        itr = self.head
        if itr == None:
            self.head = Node(data, itr)
            return
        while itr.next:
             itr = itr.next

        itr.next = Node(data,None)

    def insertValues(self,datass):
        for i in datass:
            self.insertintolistback(i)

    def removeIthElement(self,i):
        itr = self.head
        count=0
        while(itr):
            if count ==i-1:
              itr.next =itr.next.next
              break
            count+=1

            itr=itr.next

    def insertAt(self,i,data):
        itr = self.head
        count = 0
        if i == 0:
            n = Node(data,self.head)
            self.head = n
            return
        while(itr):
            if count==i-1:
                temp = Node(data,itr.next)
                itr.next = temp
                break
            count += 1

            itr = itr.next





l = Linkedlist()
li = ['mango','orange','pineapple','citaphal','rasberry']
l.insertValues(li)
l.removeIthElement(4)
'''l.insertAt(0,'strawberry')
l.insertAt(6,'strawberry')'''
l.printlinkedlist()