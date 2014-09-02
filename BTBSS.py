__author__ = 'butterfly'

#min,max
#max,min
#min,max,min max
#min,max,...min.
#min,max,min1,max1,...min,
#10,20,5,16,3,7
#max1,max2,max3

#,15,11,13,12,22,15,14,12,11,11,14

#11,13

#[15,11]
#[11,13]
#[13,12]
#[12,22]
#[22,15,14,12,11,11]
#[22,11]
#[11,14]
#15,12，13，【20，15，14，12，11，10】，14
#20],[10
#12,20,
#1,3,4
#min = 1 profit = 0
#profit = 3 - 1 >0?3-1:0
#profit = 2
#min = 3 < 1?3:1
#min = 1
#profit 0
#profit 1 min 12
#profit 8 min 12
#profit 3 min 2
#profit 2  min 12
#profit 0 min 12
#profit -1 min 11
#profit -1 min 10
#prfoit 4 min 10

#profit 8

class Solution:
    def zip(self,array):
        size = len(array)
        cloned = []
       # cloned.append(array[0])
        i = 0
       # value1 = array[start]
        while i < size:
            value = array[i]
            cloned.append(value)
            j = i + 1
            flag = False
            while j<size and array[j]<=value:
                value = array[j]
                flag = True
                j = j + 1
            if flag:
                cloned.append(array[j-1])
            i = j

        return cloned

    def getMax(self,array,start,end):
        #if start>end:
         #   return [0,start]
        max = array[start]
        index = start
        for i in range(start,end):
            if array[i] > max:
                max = array[i]
                index = i
        return [max,index]
    def getMin(self,array,start,end):
        #if start
        min = array[start]
        index = start
        for i in range(start,end):
            if array[i] < min:
                min  = array[i]
                index = i
        return [min,index]
    def maxRes(self,a,b):
        if a>b:
            return a
        else:
            return b
    #assume end>start
    def dfs(self,array,start,end):
        max = self.getMax(array,start,end)
        min = self.getMin(array,start,end)
       # print("one travel")
        #print(max)
        #print(min)
        if max[1] >= min[1]:
            return max[0] - min[0]
        else:
            #if min.index == end -1:
            max1 = self.dfs(array,0,max[1]+1)
            max2 = self.dfs(array,max[1]+1,min[1])
            max3 = self.dfs(array,min[1],end)
            max = self.maxRes(max1,max2)
            max = self.maxRes(max,max3)
            return max
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        array = self.zip(prices)
        print(array)
        return self.dfs(array,0,len(array))
        #return max'

#print(Solution().maxProfit([2,4,1]))