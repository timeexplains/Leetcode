class Solution:
    def  convertToStr(self,s):
        str = ""
        for ch in s:
            if ch>='A' and ch <='Z':
              #  print(ch)
                ch = ch.lower()
              #  print(ch)
                str = str + ch
            elif ch>='a' and ch<='z':
                str = str + ch
            elif ch>='0' and ch<='9':
                str = str + ch
            else:
                continue
        return str
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = self.convertToStr(s)
        low = 0
        high = len(s) - 1

        flag = True
        while low<high:
            if s[low] != s[high]:
                flag = False
                break
            low = low + 1
            high = high -1
        return flag

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))