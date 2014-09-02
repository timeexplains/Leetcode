__author__ = 'butterfly'


class Solution:
    def binarySearch(self,A,target):
        low = 0
        high = len(A)  - 1

        while low <=high:
            mid = (low + high) >> 1
            if A[mid] >target:
                high = high - 1
            elif A[mid] == target:
                ans = mid
                break
            else:
                low = low + 1
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            return mid
        else:
            return mid + 1


    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        return self.binarySearch(A,target)