__author__ = 'butterfly'

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None:
            return None
        n = 0
        p = head
        while p != None:
            n = n + 1
            p = p.next

        p = head
        index = 0
        list1 = []
        list2 = []
        while p != None:
            #print("val is:%d,n/2 is:%d,index is:%d,n mod 2 is:%d"%(p.val,int(n>>1)+int(n%2),index,n%2))
            if index < int(n>>1)+n%2:
                list1.append(p)
            else:
                list2.append(p)
            p = p.next
            index = index + 1

        list2.reverse()

        num = int(n>>1)
        index = 0

       # print("n is:%d,n/2 is:%d"%(n,num))
#        print("list 1 is:")
 #       for element in list1:
  #          print(element.val)

   #     print("list 2 is:")
    #    for element in list2:
     #       print(element.val)

        #node1 = list1[0]
        while index < num+ n%2:
            node1 =  list1[index]
            print("n is %d,index is:%d,num is:%d"%(n,index,num+n%2))
            if index >=num:
                node1.next = None
                break
            #break
            node2 = list2[index]
            node1.next = node2
            index = index + 1
            if index >= num + n%2:
                node2.next = None
                break
#            print("n/2 is :%d,index is:%d"%(index,n>>1+n%2))
            node1 = list1[index]
            node2.next = node1

        return head

r = ListNode(1)
r1 = ListNode(2)
r2 = ListNode(3)
r3 = ListNode(4)
r4 = ListNode
r.next = r1
r1.next = r2
#r2.next = r3
def printF(root):
    while root != None:
        print(root.val)
        root = root.next
printF(Solution().reorderList(r))






