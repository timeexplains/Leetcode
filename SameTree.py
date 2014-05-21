__author__ = 'butterfly'


# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None and q!= None:
            return False
        elif p != None and q == None:
            return False
        else:
            if p.val != q.val:
                return False
            flag = self.isSameTree(p.left,q.left)
            flag2 = self.isSameTree(p.right,q.right)
            return flag&flag2
        