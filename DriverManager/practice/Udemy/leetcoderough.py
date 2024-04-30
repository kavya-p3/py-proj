Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def comparetrees(self, tree1, tree2):
        k1 = tree1
        k2 = tree2
        while k1 and k2:
            if k1.val != k2.val:
                return False
            k1 = k1.left
            k2 = k2.right
        k3 = tree1
        k4 = tree2
        while k3 and k4:
            if k3.val != k4.val:
                return False
            k3 = k3.right
            k4 = k4.left
        if k3 or k4 or k1 or k2:
            return False
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return (self.comparetrees(root.left, root.right))

s=Solution()
s.isSymmetric()
