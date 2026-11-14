class Solution:
    def isValid(self, s: str) -> bool:
        dic={
            ']':'[',
            '}':'{',
            ')':'('
        }
        stack=[]
        for ch in s:
            if ch == '{' or ch=='[' or ch=='(':
                stack.append(ch)
            else:
                if stack and dic[ch] == stack[-1]:
                    stack.pop()
                else: 
                    return False
        return not stack
