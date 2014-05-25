__author__ = 'butterfly'

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
   # def __init__(self):
    #    return

    def init(self,n):
        self.marked = []
        self.cnt = 0
        self.treelist = []
        for i in range(n+1):
            self.marked.append(False)
        return

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


    def expand(self,n,num,root,depth):
        treelist = []
        queue = []
        root.index = 1
        root.parent = None
        queue.append(root)
        size = 1
        while size > 0:
            node = queue.pop(0)
            size = size - 1
            #isLeaf = True
            if node.left != None:
                node.left.parent = node
                node.left.index = node.index*2
                queue.append(node.left)
                size = size + 1
                #isLeaf = False
            if node.right != None:
                node.right.parent = node
                node.right.index = node.index*2 + 1
                queue.append(node.right)
                size = size + 1
                #isLeaf = False
            #if isLeaf and can
            if node.left == None :
                leafnode = TreeNode(num)
                leafnode.parent = node
                leafnode.index = node.index*2
                node.left = leafnode
                if self.isValidBST1(leafnode):
                    #tree = TreeNode(root.val)
                    #tree.left = root.left
                    #tree.right = root.right
                    #treelist.append(tree)
                    self.visit(n,root,depth+1)
                node.left = None
            if node.right == None:
                leafnode = TreeNode(num)
                leafnode.parent = node
                node.right = leafnode
                leafnode.index = node.index*2 + 1
                #self.cloneTree(root)
                if self.isValidBST1(leafnode):
                    #tree = TreeNode(root.val)
                    #tree.left = root.left
                    #tree.right = root.right
                    self.visit(n,root,depth+1)
                node.right = None

    def isValidBST1(self,leafnode):
        num = leafnode.val
        #while leafnode.parent != None:
        parent1 = leafnode.parent
        if parent1.index*2 == leafnode.index and num < parent1.val:
            parent2 = parent1.parent
            if parent2 == None:
                return True
            elif parent2.index*2 == parent1.index:
                return True
            elif parent2.index*2 + 1 == parent1.index and num > parent2.val:
                return True
            else:
                return False
        elif parent1.index*2 +1 == leafnode.index and num > parent1.val:
            parent2 = parent1.parent
            if parent2 == None:
                return True
            elif parent2.index*2 + 1 == parent1.index:
                return True
            elif parent2.index*2 == parent1.index and num < parent2.val:
                return True
            else:
                return False
        else:
            return False

    def outPrint(self,level):
        #for i in range(len(level)):
         print(level)

    def cloneTree(self,root):
        if root == None:
            return None
        cloneRoot = TreeNode(root.val)
        if root.left != None:
            cloneRoot.left = self.cloneTree(root.left)
        if root.right != None:
            cloneRoot.right = self.cloneTree(root.right)
        return cloneRoot

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
                self.outPrint(level)
                level=[]
            if node.left != None:
                queue.append(node.left)
                size = size + 1
            if node.right != None:
                queue.append(node.right)
                size = size + 1
        return

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

    def containsTree(self,root):
        index = 0
        flag = False
        #print("before comparen1");
        self.levelPrint(root)
        #print("comparent begin:")
        while index < self.cnt:
            if self.isSameTree(self.treelist[index],root):
                #print("treelist[%d] is"%index)
                self.levelPrint(self.treelist[index])
                #print("treelist[%d] end:"%index)
                self.levelPrint(root)
                #print("same end!")
                flag = True
                break
            index = index + 1
        #print("comparent end:")
        return flag

    def visit(self,n,root,depth):
       # print("Depth :%d"%depth)
        if depth == n:
            set = self.inorderTravel(root)
           # print("%d,%d,%d"%(set[0].val,set[1].val,set[2].val))
            #print("case %d"%self.cnt)
           # self.levelPrint(root)
            cloneRoot = TreeNode(root.val)
            cloneRoot.left = root.left
            cloneRoot.right = root.right
            if self.containsTree(root) ==  False:
                #cloneRoot = self.cloneTree(root)
                self.treelist.append(cloneRoot)
                #self.levelPrint(self.treelist[self.cnt])
                #self.levelPrint(root)
                self.cnt = self.cnt + 1
           # print("cnt=%d"%self.cnt)
            return
        #if depth >=n+1:
         #   self.cnt = self.cnt + 1
          #  self.treelist.append(root)
           # return
        for num in range(1,n+1):
            if self.marked[num] == False:
                self.marked[num] = True
                self.expand(n,num,root,depth)
                #treelist = self.expand(num,root)
                #for tree in treelist:
                #   self.marked[num] = True
                #  self.visit(n,tree,depth+1)
                self.marked[num] = False
    def differeNode(self):
        result = []
        for i in range(self.cnt):
           node1 = self.treelist[i]
           flag = False
           for j in range(i+1,self.cnt):
               node2 = self.treelist[j]
               if self.isSameTree(node1,node2):
                   flag = True
                   break
           if flag == False:
               result.append(node1)
        return result

    # @return a list of tree node
    def generateTrees(self, n):
        self.init(n)
        for i in range(1,n+1):
            root = TreeNode(i)
            self.marked[i] = True
            self.visit(n,root,1)
            self.marked[i] = False
        for i in range(0,len(self.treelist)):
            print("case %d"%(i+1))
            self.levelPrint(self.treelist[i])
        #return len(self.treelist)
        return self.treelist
        #return self.cnt

#print(Solution().generateTrees(3))