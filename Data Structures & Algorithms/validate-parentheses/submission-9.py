class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        dic= {
            "(":")",
            '{':'}',
            "[":"]"
        }
        stack = []
        for ch in s:
            if ch in dic:
                stack.append(ch)
            else:
                if stack and ch == dic[stack[-1]]:
                    stack.pop()
                else:
                    return False
            
        if not stack:
             return True
        return False
