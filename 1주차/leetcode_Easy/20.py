'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

- 내 처음 답
단순 열린괄호, 닫힌괄호의 갯수만 비교, "([)]"의 경우 false인데 내 답은 true

from collections import Counter

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_dict = dict(Counter(s).most_common())
        boolVal = True

        if str_dict.setdefault('(',-1) != str_dict.setdefault(')',-1):
                boolVal =  False
        elif str_dict.setdefault('{',-1) != str_dict.setdefault('}',-1):
                boolVal =  False
        elif str_dict.setdefault('[',-1) != str_dict.setdefault(']',-1):
                boolVal =  False
             
        return boolVal

'''

class Solution:
    def isValid(self, s):
        stack=[]
        brackets={'}':'{',')':'(',']':'['}
        for bracket in s:
            if bracket in brackets.values(): #Opening bracket 
                stack.append(bracket)
            else:# Closing bracket
                if stack and brackets[bracket]==stack[-1] :  
                    stack.pop()
                else: 
                    return False
        
        if stack:
            return False
        return True
