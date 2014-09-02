__author__ = 'butterfly'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def travel(self,root):
        if root == None:
            tmp = object()
            tmp.head = None
            tmp.tail = None
            return tmp
        leftNode = self.travel(root.left)
        rightNode = self.travel(root.right)
        #flag = False
        set = [root,root]

        if leftNode.head != None and rightNode.head != None:
            root.right = leftNode.head
            leftNode.tail.right = rightNode.head
            root.left = None
            tmp = object()
            tmp.head = root
            tmp.tail = rightNode.tail
            return tmp
        elif leftNode.head != None:
            root.right = leftNode.head
            root.left = None
            tmp = {}
            tmp.head = root
            tmp.tail = leftNode.tail
            return tmp
        elif rightNode.head != None:
            root.right = rightNode.head
            root.left = None
            tmp = object()
            tmp.head = root
            tmp.tail = rightNode.tail
            return tmp
        else:
            tmp = object()
            tmp.head = root
            tmp.tail = root
            return tmp

    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.travel(root)