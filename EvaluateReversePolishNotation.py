__author__ = 'butterfly'

#import math
#please note that int function in python different version . has different result.
class Solution:
    def isOperator(self,o):
        if o == "+" or o == "-" or o == "*" or o== "/":
            return True
        return False
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        dataStack = []
        index = 0
        for i in range(len(tokens)):
            obj = tokens[i]
            length = len(tokens)
            if self.isOperator(obj):
                index = index + 1
                data1 = int(dataStack.pop(0))
                data2 = int(dataStack.pop(0))
                if obj == "+":
                    result = data1 + data2
                elif obj == "-":
                    result = data2 - data1
                elif obj == "*":
                    result = data1*data2
                else:
                    result = int(abs(data2)/abs(data1))
                    if data2 * data1 < 0:
                        result = result * -1
                        #result =  self.floor(data2,data1)
                #if(length == 13 and obj == "/"):
                #print((int)(6/-132))
                dataStack.insert(0,result)
            else:
                dataStack.insert(0,int(obj))
        return int(dataStack[0])

#print(Solution().evalRPN([2,1,"+",3,"*"]))
#print(Solution().evalRPN([4,13,5,"/","+"]))
#print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))