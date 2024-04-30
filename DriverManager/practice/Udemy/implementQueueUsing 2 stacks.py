class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,item):
        self.stack1.append(item)

    def deque(self):
        for i in range(len(self.stack1)-1):
            self.stack2.append(self.stack1.pop())

        item= self.stack1.pop()
        print('popped item',item)
        for i in range(len(self.stack2)):
            t = self.stack2.pop()
            self.stack1.append(t)

    def printqueue(self):
        for i in range(0,len(self.stack1)):
            print(self.stack1[i])

q = Queue()
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
q.deque()
q.enqueue(6)
q.enqueue(7)
q.deque()
q.deque()

q.printqueue()

