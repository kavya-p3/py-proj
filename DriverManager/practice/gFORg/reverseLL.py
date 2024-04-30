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

    def removeIthElement(self,i):
        itr = self.head
        count=0
        if i==0:
          temp = itr.data
          self.head=itr.next
          return temp
        while(itr):
            if count ==i-1:
              temp = itr.data
              itr.next =itr.next.next
              break
            count+=1

            itr=itr.next

        return temp


    def revesell(self):

        i = 0
        n = 4
        while n>-1:
            temp=self.removeIthElement(0)
            self.insertAt(n,temp)
            n-=1




l = Linkedlist()
li = ['mango','orange','pineapple','citaphal','raspberry']
l.insertValues(li)
l.printlinkedlist()
print()
l.revesell()
l.printlinkedlist()
