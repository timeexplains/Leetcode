__author__ = 'butterfly'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printF(self,head,node):
        print("node is:%d"%node.val)
        print("case:")
        t = head
        while head:
            print(head.val)
            if head == node:
                break
            head = head.next
        #print("case end:")
##        print("whole is:")
        #while t != None:
  #          print(t.val)
   #         t = t.next

    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        node = head
        nodePrev = None
        index = 1
        while node:
            #if nodePrev == None:
             #   nodePrev = node
              #  node = node.next
               # continue
            #nextNode = node.next
#            self.printF(head,node)
            h  = head
            prev = None

            #print(node.val)
            index = index + 1
            if index > 11:
                break
            while h != node:
                if h.val > node.val:
                    break
                prev = h
                h = h.next

            if h == node:
                #print("in place:"+str(node.val))
                nodePrev = node
                node = node.next
                continue
            if prev:
                #print("from prev:"+str(prev.val))
                nodePrev.next = node.next
                prev.next = node
                node.next = h
            else:
                #print("to Head:"+str(head.val))
                nodePrev.next = node.next
                node.next = head
                head = node
            node = nodePrev.next
            #print(node.val)
        return head







