__author__ = 'butterfly'

class Solution:
    def isPalindrome(self,st,start,end):
        s = st[start:end+1];
        try:
            result = self.map[(start,end)]
            return result
        except:
            low = 0
            high = len(s)-1
            result = True
            while low<high:
                if s[low] == s[high]:
                    low = low + 1
                    high = high -1
                else:
                    result = False
                    break
            self.map[(start,end)] = result
            return result

    def minCut(self,s):
        result = []
        maxSplit = len(s)
        result.append(0)
        self.map =  dict()
        for i in range(1,maxSplit):
            result.append(i)
        for i in range(2,maxSplit):
            for j in range(1,i):
                subStr = s[j:i+1]#substring
                if self.isPalindrome(subStr):
                    if result[j-1] + 1 < result[i]:
                        result[i] = result[j-1] + 1
        return result[maxSplit-1]


#print(Solution().minCut("bb"))
#s = "abcdefg"
#len1 = len(s) -1
#print(s[1:len1])
#print(Solution().minCut(s[1:len1+1]))