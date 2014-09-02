__author__ = 'butterfly'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#Leaf node . max value = val
#parent node. max node + val


class Solution:
    def getMaxValue(self,left1,right1,val):
        #left1 = result1[1]
        #right1 = result1[2]
        val1 = val
        if left1>right1 and left1>0:
            val1 = val1 + left1
        elif right1>=left1 and right1>0:
            val1 = val1 + right1
        else:
            val1 = val1 + 0
        return val1

    def maxPathSum1(self,root):
        if root == None:
            return [0,0,0]
        try:
            result = root.calculated
            return result
        except:
            if root.left == None and root.right == None:
                 self.allResult.append(root.val)
                 #.map[root] = [root.val,0,0]
                 root.calculated = [root.val,0,0]
                 return [root.val,0,0]
            val1 = 0
            if root.left != None:
                 result1 = self.maxPathSum1(root.left)
                 result = result1[0]
                 val1 = self.getMaxValue(result1[1],result1[2],root.left.val)
           # self.allResult.append(result)
            val2 = 0
            if root.right != None:
                result2 = self.maxPathSum1(root.right)
                result = result2[0]
                val2 = self.getMaxValue(result2[1],result2[2],root.right.val)
            #self.allResult.append(result)
            val = root.val
            if val1>0:
                val = val1 + val
            if val2>0:
                val = val2 + val
            self.allResult.append(val)
            root.calculated = [val,val1,val2]
            return [val,val1,val2]

    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        #result = root.val
        self.map = dict()
        self.allResult = []
        self.maxPathSum1(root)
        result = self.allResult[0]
        for element in self.allResult:
            if element >result:
                result = element
        return result
