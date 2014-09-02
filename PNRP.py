__author__ = 'butterfly'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def bfs(self,root):
        expandSet = []
        expandSet.append(root)

        size = 1
        depth = 0
        pNode = root
        #levelSize = 1
        while( size > 0):
            node = expandSet.pop(0)
            size = size - 1
           # levelSize = levelSize - 1
            if size == 0:
                depth = depth + 1
            else:
                pNode.next = node
                pNode = node
            if node.left != None:
                expandSet.append(node.left)
                size = size + 1
            if node.right != None:
                expandSet.append(node.right)
                size = size + 1
           # pNode = node


    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        self.bfs(root)