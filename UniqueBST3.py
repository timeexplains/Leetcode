class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def transform(self,treelist,n):
        result = []
        for tree in treelist:
            set = self.buildTreeList(tree,n)
            result.extend(set)
        return result

    def cloneTree(self,tree):
        if tree == None:
            return None
        node = TreeNode(tree.val)
        if tree.left != None:
            node.left = self.cloneTree(tree.left)
        if tree.right != None:
            node.right = self.cloneTree(tree.right)
        return node



    def buildTreeList(self,tree,n):
        result = []
        tree1 = TreeNode(n)
        tree1.left = tree
        result.append(tree1)

        node = tree
        while node != None:
            rightNode = node.right
            allocationNode = TreeNode(n)
            allocationNode.left  = rightNode
            node.right = allocationNode

            result.append(self.cloneTree(tree))

            node.right = rightNode
            allocationNode.left = None


            node = node.right
        return result




    def generateTrees(self,n):
        if n == 0:
            result = []
            result.append(None)
            return result
        if n == 1:
            result = []
            result.append(TreeNode(1))
            return result
        else:
            return self.transform(self.generateTrees(n-1),n)

    def numTrees(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            result = 0
            for i in range(n):
                result = self.numTrees(i)*self.numTrees(n-i-1) + result
            return result
    
    def levelPrint(self,root):
        queue = []
        size = 1
        queue.append(root)
        level = []
        #level.append(root)
        while size > 0:
            node = queue.pop(0)
            size = size - 1
            level.append(node.val)
            if size == 0:
                print(level)
                level=[]
            if node.left != None:
                queue.append(node.left)
                size = size + 1
            if node.right != None:
                queue.append(node.right)
                size = size + 1
        return

ans = Solution().generateTrees(3)
index  = 1
for tree in ans:
    print("case %d"%index)
    Solution().levelPrint(tree)
    index = index + 1







