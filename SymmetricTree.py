__author__ = 'openg'


# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Queue:
    def __init__(self):
        self.queue = []
    def push(self,x):
        self.queue.append(x);
    def pull(self):
        self.queue.pop(0)
    def getFront(self):
        self.queue[0]
    def isEmpty(self):
        return len(self.queue)

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        print("aaaaaa!")
        arraylist = self.tagByBfs(root)
        print("bbbbbb!")
        return self.assertSymmetric(arraylist)

    def pair(self,index):
        level = self.calculateLevel(index)
        return 1<<(level+1) - 1 + 1<<level - index

    def calculateLevel(self,index):
        level = 0
        while True:
            start = 1<<level
            end = (1<<(level+1))
            end = end - 1
            print(start)

            if index >= start and index<=end:
                return level
                break
            level = level + 1

    def assertSymmetric(self,arraylist):
        head = 0
        tail = len(arraylist)

        print(head)
        print(tail)
        for index in range(0,tail):
            pairIndex = self.pair(index)
            print("ccccc!")
            if arraylist[index] != arraylist[pairIndex]:
                return False

    def tagByBfs(self,root):
        index = 0
        arraylist = []
        root.index = index
        arraylist.append(root)
        q = Queue()
        q.push(root)
        while q.isEmpty()==False:
            node = q.pull()
            index = index + 1
            node.index = index
            arraylist.append(node)
            if node.left != None:
                q.push(node.left)
            if node.right != None:
                q.push(node.right)
        return arraylist



print(Solution().isSymmetric(TreeNode(1)))

#print(Solution().isSymmetric(None));

