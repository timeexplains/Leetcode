__author__ = 'butterfly'

# Definition for a undirected graph node
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
class Solution:
    def cloneNode(self,node):
        cloned = UndirectedGraphNode(node.label)
        #cloned.neighbors = []
        return cloned
    def clone(self,node):
        if node == None:
            return None
        try:
            cloned = self.map[node.label]
            return cloned
        except:
            cloned = self.cloneNode(node)
            if len(node.neighbors)<=0:
                #cloned.neighbors.append(cloned)
                self.map[node.label] = cloned
                return cloned
            for elementNode in node.neighbors:
                 if elementNode.label == node.label:
                     cloned.neighbors.append(cloned)
                 else:
                     cloned.neighbors.append(self.clone(elementNode))
            self.map[node.label] = cloned
            return cloned


    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        self.map = dict()
        return self.clone(node)


