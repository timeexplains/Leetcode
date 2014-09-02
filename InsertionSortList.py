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
            self.printF(head,node)
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
                print("in place:"+str(node.val))
                nodePrev = node
                node = node.next
                continue
            if prev:
                print("from prev:"+str(prev.val))
                nodePrev.next = node.next
                prev.next = node
                node.next = h
            else:
                print("to Head:"+str(head.val))
                nodePrev.next = node.next
                node.next = head
                head = node
            node = nodePrev.next
            #print(node.val)
        return head

root = ListNode(9)
root1 = ListNode(8)
root2 = ListNode(7)
root3 = ListNode(6)
root4 = ListNode(5)
root5 = ListNode(4)
root6 = ListNode(3)
root7 = ListNode(2)
root8 = ListNode(1)
root9 = ListNode(0)


root.next = root1
root1.next = root2
root2.next = root3
root3.next = root4
root4.next = root5
root5.next = root6
root6.next = root7
root7.next = root8
root8.next = root9

node = Solution().insertionSortList(root)
while node:
    print(node.val)
    node = node.next







