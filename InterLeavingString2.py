__author__ = 'butterfly'

class Solution:
    def findLargestStr(self,s,index,end,s3,index3,end3):
        result = ""
        while index < end and index3 < end3:
            if s[index] != s3[index3]:
                break
            result = result + s[index]
            index = index + 1
            index3 = index3 + 1
        return result

    def match(self,s1,index1,end1,s2,index2,end2,s3,index3,end3):
        if index3 >= end3:
            return True
        if end1 - index1 + end2 - index2 < end3 - index3:
            return False
        common1  = self.findLargestStr(s1,index1,end1,s3,index3,end3)
        len1 = len(common1)
        common2 = self.findLargestStr(s2,index2,end2,s3,index3,end3)
        len2 = len(common2)


        #print(common1)

        flag = False
        if len1 > 0 and len1 >= len2:
            length = len1
            print(common1)
          #  commonStr = common1[:length]
         #   print(commonStr)
           # self.cnt = self .cnt + 1
            #if self.cnt > 10:
             #   break
            flag = self.match(s1,index1+length,end1,s2,index2,end2,s3,index3+length,end3)
            if flag:
                return True
                #return True
        if flag:
            return True

        #print(common2)
        if len2 > 0 and len2 > len1 :
           length = len2
           print(common2)
            #commonStr = common2[:pos]
           flag = self.match(s1,index1,end1,s2,index2+length,end2,s3,index3+length,end3)
           if flag:
                return True
        return flag




    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        #self.cnt = 0
        return self.match(s1,0,len(s1),s2,0,len(s2),s3,0,len(s3))

print(Solution().isInterleave("a","b","ab"))
print(Solution().isInterleave("aabcc","dbbca","aadbbcbcac"))
print(Solution().isInterleave("aabcc","dbbca","aadbbbaccc"))
#"aabaac", "aadaaeaaf", "aadaaeaabaacaaf"
print(Solution().isInterleave("aabaac", "aadaaeaaf", "aadaaeaabaacaaf"))
print(Solution().isInterleave("bcbccabcccbcbbbcbbacaaccccacbaccabaccbabccbabcaabbbccbbbaa", "ccbccaaccabacaabccaaccbabcbbaacacaccaacbacbbccccbac", "bccbcccabbccaccaccacbacbacbabbcbccbaaccbbaacbcbaacbacbaccaaccabcaccacaacbacbacccbbabcccccbababcaabcbbcccbbbaa"))
