class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def createcopy(self, head):
        if head is None :
            return
        node = Node(head.val)
        node.next = head.next
        head.next = node
        head = node.next
        self.createcopy(head)
        return node

    def setRandom(self, head, clone):
        while head.next and head.next.next and clone:
            clone.random = head.random.next
            head = head.next.next
            clone = clone.next.next

    def unweave(self, head, clone):
        while head.next and head.next.next and clone:
            head.next = clone.next
            clone.next = head.next.next
            head = head.next
            clone = clone.next

    def copyRandomList(self, head) :
        if head is None:
            return None
        clonestart = self.createcopy(head)
        self.setRandom(head, clonestart)
        self.unweave(head, clonestart)
        return clonestart

s=Node(4)
s1=Node(7)
s2=Node(-2)
s.next=s1
s1.next=s2
s.random=s2
s1.random=s

k=Solution()
z=k.copyRandomList(s)
print()
