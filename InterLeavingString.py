__author__ = 'butterfly'

class Solution:
    def match(self,s1,index1,end1,s2,index2,end2,s3,index3,end3):
        if index3 == end3:
            return True
        if end1 - index1 + end2 - index2 < end3 - index3:
            return False
        char = s3[index3]
        flag = True
        if index1<end1 and  s1[index1] == char:
            flag1 =  self.match(s1,index1+1,end1,s2,index2,end2,s3,index3+1,end3)
            if flag1:
                return True
        if index2<end2 and s2[index2] == char:
            flag2 = self.match(s1,index1,end1,s2,index2+1,end2,s3,index3+1,end3)
            if flag2:
                return True
        if index1 < end1 -1:
            flag3 = self.match(s1,index1+1,end1,s2,index2,end2,s3,index3,end3)
            if flag3:
                return True
        if index2 < end2 - 1:
            flag4 = self.match(s1,index1,end1,s2,index2+1,end2,s3,index3,end3)
            if flag4:
                return True
        if index1 < end1 -1 and index2 <end2 -1:
            flag5 = self.match(s1,index1+1,end1,s2,index2+1,end2,s3,index3,end3)
            if flag5:
                return True
        #flag6 = self.match(s1,index)
        #flag6 = self.match(s1,index1+1,end1,s2)
        return False


    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        return self.match(s1,0,len(s1),s2,0,len(s2),s3,0,len(s3))


print(Solution().isInterleave("a","b","ab"))
print(Solution().isInterleave("aabcc","dbbca","aadbbcbcac"))
print(Solution().isInterleave("aabcc","dbbca","aadbbbaccc"))
#"aabaac", "aadaaeaaf", "aadaaeaabaacaaf"
print(Solution().isInterleave("aabaac", "aadaaeaaf", "aadaaeaabaacaaf"))
print(Solution().isInterleave("bcbccabcccbcbbbcbbacaaccccacbaccabaccbabccbabcaabbbccbbbaa", "ccbccaaccabacaabccaaccbabcbbaacacaccaacbacbbccccbac", "bccbcccabbccaccaccacbacbacbabbcbccbaaccbbaacbcbaacbacbaccaaccabcaccacaacbacbacccbbabcccccbababcaabcbbcccbbbaa"))
