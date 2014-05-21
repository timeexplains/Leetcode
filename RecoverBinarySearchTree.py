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
        size = len(set)
        i = 0
        j = 0
        while i < (size-1):
            a = set[i].val
            b = set[i+1].val
            if b < a:
                swapI = i
                break
            i = i + 1
        j = swapI + 1
        swapJ = j
        while j < size - 1:
            a = set[j].val
            b = set[j+1].val
            if a > b:
                swapJ = j + 1
                break
            j = j + 1
        tmp  = set[swapI].val
        set[swapI].val = set[swapJ].val
        set[swapJ].val = tmp



    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        result = self.inorderTravel(root)
        self.scan(result)
        return root
