__author__ = 'butterfly'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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