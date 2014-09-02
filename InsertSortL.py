__author__ = 'butterfly'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
   # def rebuildList(self,head,findPrev,findNext,node,nodePrev):

    #    return [head,nodePrev]
    def binarySearch(self,A,n,node):
        if n<0:
            return [None,node,0]
        low = 0
        high = n
       # mid = (low + high) / 2
        find = -1
        while low <= high:
            mid = (low + high  - (low+high)%2) >>1
            if A[mid].val > node.val:
                find  = mid
                break
            else:
                low = mid + 1
        if find == -1:
            return [A[n],node,n+1]
        else:
            if find == 0:
                preNode = None
            else:
                preNode = A[find-1]
            return [preNode,A[find],find]
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        node = head
        nodePrev = None
        index = -1
        A = []
        while node != None:

            #nextNode = node.next
            searchResult = self.binarySearch(A,index,node)
            #index = index + 1
            findNext = searchResult[1]
            findPrev = searchResult[0]
            insertPos = searchResult[2]

 #           print("node val is:%d,findNext val is:%d,insert pos is:%d"%(node.val,findNext.val,insertPos))

            A.append(node)
            for j in range(insertPos,index+1):
                 end = index - j + insertPos
                 A[end+1] = A[end]
            A[insertPos] = node
            index = index + 1
            node = node.next

        for i in range(0,index+1):
#            print(A[i].val)
            if i != 0:
                A[i-1].next = A[i]
        return A[0]



root = ListNode(4)
root1 = ListNode(2)
root2 = ListNode(1)
root3 = ListNode(3)

root.next = root1
root1.next = root2
root2.next = root3

r = Solution().insertionSortList(root)#
#while r !=None:
#   print(r.val)
 #  r = r.next
#print(Solution().insertionSortList(root).val)






