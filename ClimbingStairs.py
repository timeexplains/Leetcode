__author__ = 'butterfly'

class Solution:
    def init(self,n,f):
        for i in range(n+2):
            f.append(0)
    def step(self,n,f):
        self.init(n,f)
        f[1] = 1
        f[2] = 2
        for i in range(3,n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]

    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        return self.step(n,[])
