__author__ = 'butterfly'

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
     def inorderTravel(self,root):
        if root == None:
            return []
        result = []
        #result.push(root)
        size = 1
        set1 = self.inorderTravel(root.left)
        result.extend(set1)
        result.append(root)
        set2 = self.inorderTravel(root.right)
        result.extend(set2)
        return result

     def scan(self,set):
        for i in range(len(set)-1):
            val1 = set[i].val
            val2 = set[i+1].val
            if val1 >= val2:
                return False
        return True

     def isValidBST(self,root):
         set = self.inorderTravel(root)
         return self.scan(set)

     def canPlace(self,index,i):
         return True

     def search(self,n,index):
         if index == n+1:
             if self.isValidBST(self.set):
                 self.cnt = self.cnt + 1
             return
         for i in range(1,n+1):
             if self.marked[i] == False and self.canPlace(self.set,index,i):
                 self.marked[i] = True
                 self.set.append(i)
                 self.search(n,index+1)
                 self.marked[i] = False



     def init(self,n):
         self.set = []
         self.marked = []
         self.cnt = 0
         for i in range(n+1):
             self.marked.append(False)

     def generateTrees(self, n):
        self.init(n)
        return self.search(n,0)