__author__ = 'butterfly'

class Solution:
    def isvalid(self,ip):
        if ip[0]=='0' and ip != "0":
            return False
        if int(ip)<0 or int(ip)>255:
            return False
        return True

    def search(self,s,start,length,depth,result):
        if depth > 4:
            if length == 0:
                self.ips.append(str(result[0]+"."+result[1]+"."+result[2]+"."+result[3]))
            return
        if length <=0:
            return

        for dlen in range(1,4):
            if dlen > length:
                break
            ip = s[start:(start+dlen)]
            if self.isvalid(ip):
                result[depth-1] = ip
                self.search(s,start+dlen,length-dlen,depth+1,result)

    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self,s):
        result = []
        if len(s)<4 or len(s)>12:
            return result
        self.ips = []
        result = []
        result.append("")
        result.append("")
        result.append("")
        result.append("")
        self.search(s,0,len(s),1,result)
        return  self.ips

#t = Solution().restoreIpAddresses("25525511135")
#for s in t:
 #   print(s)
