__author__ = 'butterfly'

#3,3,3,4,4,4,5,5,5,6,6,6,7
#3op3op3 = 1
#3&3 = 3
#11,11,11 =
#3,7,3,4,3.
#
#bit[3] =
#bit[32] = bit[0]  = 8

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        bit = []
        nbit = []
        table = []
        for i in range(32):
            bit.append(0)
            nbit.append(0)
            table.append(1<<i)
        for element in A:
            num = int(element)
            base = 0
            if num >0:
                set = bit
            else:
                set  = nbit
            while num!=0:
                digit=int(abs(num)%2)
                set[base] = (set[base] + digit)%3
               # print((num,base,digit))
                #print((num,digit))
                #print("bit ")
                base = base + 1
                num = int((abs(num)-digit)/2)
                #print(num)
                #if
        for i  in range(32):
         #   print
            result = result  + table[i]*bit[i]
       # for i in range(32):
            result = result - table[i]*nbit[i];
        return result

print(Solution().singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))
#print(-3%2)
#-3,3,3,3