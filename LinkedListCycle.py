__author__ = 'butterfly'

#aXXXXXXXXXbcdefghijklmn0123456789
#map[node,True],
#          bcdefghijklmn0123456789
#          b
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        map = dict()
        result = False
        while head != None:
            try:
                val = map[head]
                result = True
            except:
                map[head] = True
            if result:
                break
            head = head.next
        return result