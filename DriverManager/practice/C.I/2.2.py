class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insertinfront(self, datas):
        for i in datas:
            n = Node(i, self.head)
            self.head = n

    def insertBack(self, datas):


        for i in datas:
            itr = self.head
            if itr == None:
                self.head = Node(i, self.head)
            else:
                while(itr.next):
                    itr=itr.next
                itr.next = Node(i, None)



    def print(self):
        itr = self.head
        while (itr):
            print(itr.data, '--->', end='')
            itr = itr.next

    def printkelements(self,k):
        itr=self.head
        count = 0
        while(itr):
            if count==k-1:
                print(itr.data,'-->',end='')
                itr= itr.next
                continue
            else:
                count+=1
                itr = itr.next


li = ['strawberry', 'mango', 'orange', 'pineapple', 'citaphal', 'raspberry']
l = Linkedlist()
l.insertBack(li)
l.printkelements(3)

