__author__ = 'butterfly'

class Solution:
    def reverseWords(self,s):
        word = ""
        words = []
        length = len(s)
        begin = True
        for i in range(length):
            if s[i] == " " and begin:
                continue
            if s[i] != " ":
                word = word + s[i]
                begin = False
            if s[i] == " " or i == length -1 and begin == False:
                words.append(word)
               # print(word)
                begin = True
                word = ""
        result = ""
        for i in range(len(words)):
            result = result + words[len(words)-i-1]
            if i != len(words) -1:
                result = result + "x "
        return result

#print(Solution().reverseWords("1 "))