__author__ = 'butterfly'

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def clone(self,head):
        node = RandomListNode(head.label)
        return node
    def copy(self,head):
        if head == None:
            return None
        try:
            result  = self.map[head.label]
            return result
        except:
            if head.next == None:
                cloned = self.clone(head)
                cloned.random = self.copy(head.random)
                return cloned
            else:
                cloned = self.clone(head)
                cloned.next = self.clone(head.next)
                cloned.random = self.clone(head.random)
                return cloned
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        self.map = dict()
        return self.copy(head)