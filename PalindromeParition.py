__author__ = 'butterfly'

class Solution:
    def isPalindrome(self,s):
        low = 0
        high = len(s)-1
        while low <high:
            if s[low] != s[high]:
                return False
            low = low + 1
            high = high - 1
        return True

    def spit(self,s,begin,length,set,depth):
        #print("length is:%d"%length)
        if depth > self.result + 1:
            return
        if length<0:
            return
        elif length == 0:
            if depth -1 < self.result:
                self.result = depth -1
#            self.ans.append(list(set))
           # print(set)
            return
      #  if depth > 10:
       #     return
        for size in range(0,length):
            size = length - size;
            if self.isPalindrome(s[begin:begin+size]) :
                print(s[begin:begin:size])
 #               set.append(s[begin:begin+size])
                self.spit(s,begin+size,length-size,set,depth+1)
  #              set.pop(depth)
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.ans = []
        self.spit(s,0,len(s),[],0)
        return self.ans

    def minCut(self,s):
        self.ans = []
        self.result = len(s) -1
        self.spit(s,0,len(s),[],0)

        return self.result


print(Solution().minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"))