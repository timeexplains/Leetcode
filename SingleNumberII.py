__author__ = 'butterfly'

#1,2,4,5,4,6,4.
#map[1] = 0


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        map = dict()
        for element in A:
            map[element] = 0
        for element in A:
            map[element] =  map[element] + 1
        for d,x in map.items():
            if x == 3:
                result = d;
                break;
        return result
