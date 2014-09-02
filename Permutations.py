__author__ = 'butterfly'

class Solution:
    def clone(self,set):
        result = []
        result.extend(set)
        return result
     #   return result

    def place(self,num,depth,set):
        if depth == len(num) + 1:
            #print(set)
            self.ans.append(self.clone(set))
        for i in num:
            if self.dict[i] == False:
                self.dict[i] = True
                set.append(i)
                self.place(num,depth+1,set)
                self.dict[i] = False
                set.pop()
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        self.dict = {}
        for digit in num:
            self.dict[digit] = False
        self.ans = []
        self.place(num,1,[])
        return self.ans

print(Solution().permute([1]))
print(Solution().permute([1,2,3]))