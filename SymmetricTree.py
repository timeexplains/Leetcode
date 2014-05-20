__author__ = 'openg'

import math
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
        return self.queue.pop(0)
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
#        print("aaaaaa!")
        arraylist = self.tagByBfs(root)
       # self.outPrint(arraylist)
        #print(len(arraylist))
 #       print("bbbbbb!")
        return self.isSytric(arraylist)

    def outPrint(self,arraylist):
        #print("arraylist is:")
        ##for i in range(len(arraylist)):
         #   print(arraylist[i].val)
       # print("arraylist end:")
       return

    def pair(self,index):
        level = self.calculateLevel(index)
        return (1<<(level+1)) - 1 + (1<<level) - index

    def isPair(self,pair1,pair2,level):
        return pair1  + pair2  ==   (1<<(level+1)) - 1 + (1<<level)

    def calculateLevel(self,index):
        level = 0
        reslevel = 0
        start = 1
  #      print(index)
       # print("index is %d"%index)
        #print("level is %")
        while index > start:
            level = level + 1
            start = 1<<level
            end = (1<<(level+1))- 1
            if index >=start and index <=end:
                reslevel = level
                break
   #         print(level)
        #print(level)
       # print("index is %d,level is:%d"%(index,reslevel))
        return reslevel

    def isSytric(self,arraylist):
        length = len(arraylist)
        marked = []
        for i in range(length):
            marked.append(False)
        index = 0
        result = True
        while index < length:
            if marked[index]:
                index = index + 1
                continue
            t2 = index
            flag = False
            marked[index] = True
            while t2 <length:
                #print("one .....")
                level = self.calculateLevel(arraylist[index].index)
                if(self.calculateLevel(arraylist[t2].index) > self.calculateLevel(arraylist[index].index) ):
                    flag = False
                    break
                elif self.isPair(arraylist[t2].index,arraylist[index].index,level) and arraylist[t2].val == arraylist[index].val :
                    flag  = True
                    marked[t2] = True
                    break
                else:
                    t2 = t2 + 1
            #print("Flag is:",flag)
            if flag == False:
                result = False
                break
            index = index  + 1
        return result

    def assertSymmetric(self,arraylist):
        head = 0
        tail = len(arraylist)

    #    print(head)
     #   print(tail)
        for index in range(0,tail):
            pairIndex = self.pair(index+1)
      #      print("ccccc!")
            #print(index + 1)
            #print(pairIndex)
      #      print("(index,pairIndex)%d%d"%(index,pairIndex))
            if self.isOutofRange(pairIndex,tail):
         #       print("from out of range!")
                return False
            #if pairIndex < 0:
                #pairIndex = tail - pairIndex - 1
            if arraylist[index].val != arraylist[pairIndex -1].val:
                return False
        return True

    def isOutofRange(self,index1,tail):
        if index1> tail or index1 < 0:
            return True
        return False

    def tagByBfs(self,root):
        index = 0
        arraylist = []
        root.index = index + 1
        q = Queue()
        q.push(root)
        while q.isEmpty()!=False:
            node = q.pull()
            #index = index + 1
            #node.index = index
            arraylist.append(node)
            if node.left != None:
                node.left.index = 2*node.index
                q.push(node.left)
            if node.right != None:
                node.right.index = 2*node.index + 1
                q.push(node.right)
        return arraylist


root = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(2)
root.left = t1
root.right = t2
t3 = TreeNode(3)
t4 = TreeNode(3)
t1.right = t3
t2.left = t4
#root.right = TreeNode(2)
#print(Solution().isSymmetric(root))

#print(Solution().isSymmetric(None));

