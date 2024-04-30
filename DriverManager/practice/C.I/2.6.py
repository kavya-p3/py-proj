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

    def print(self):
        itr = self.head
        while (itr):
            print(itr.data, '--->', end='')
            itr = itr.next

    def recurse(self,itr,length):
        if (length==0 or length==1):
            return itr.next

        self.recurse(self.head.next,length-1)
        if self.head.data == itr.data:
            print('yes',itr.data)
            itr.data=itr.next.data


l = [1,0,1,0,1]
d = Linkedlist()
d.insertinfront(l)
#d.print()
d.recurse(d.head,4)