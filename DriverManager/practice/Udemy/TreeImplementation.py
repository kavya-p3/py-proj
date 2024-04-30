class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.left=None
        self.right=None


    def insertLeft(self,data):
        if self.left==None:
            self.left=BinaryTree(data)

        else:
            t=BinaryTree(data)
            t.left=self.left
            self.left=t

    def insertRight(self,data):
        if self.right==None:
            self.right=BinaryTree(data)

        else:
            t=BinaryTree(data)
            t.right=self.right
            self.right=t

    def returnRight(self):
        return self.right

    def printTree(self):
        t=self.left
        while(t):
            print(t.key)
            t=t.left




r=BinaryTree(5)
r.insertLeft(6)
r.insertLeft(7)
r.insertLeft(8)
r.printTree()