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
                while (itr.next):
                    itr = itr.next
                itr.next = Node(i, None)

    def print(self):
        itr = self.head
        while (itr):
            print(itr.data, '--->', end='')
            itr = itr.next

    def addEle(self,head2):
        d=[]
        itr1 = self.head
        itr2 = head2
        while(itr1):
            d.append(itr1.data + itr2.data)
            itr1 = itr1.next
            itr2 = itr2.next


        return d




li = (6,)
l2 = (5,9,2)
l = Linkedlist()
l.insertBack(li)
ll =Linkedlist()
ll.insertBack(l2)

l.print()
print(" ")
ll.print()
print(" ")
it1 = l.head
it2 = ll.head
lll = Linkedlist()
temp = []
t=0
while it2:
    if it1==None:
        temp.append(t+it2.data)
        it2 = it2.next
        continue
    x = it1.data+it2.data+t
    u = x%10
    t = int(x/10)
    temp.append(u)
    it2=it2.next
    it1=it1.next
    if (it1==None and it2==None):
        temp.pop()
        temp.append((x))

lll.insertBack(temp)
lll.print()





