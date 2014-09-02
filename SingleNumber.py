__author__ = 'butterfly'

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for element in A:
            result = result^element
        return result