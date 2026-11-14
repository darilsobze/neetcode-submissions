class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = False
        formated_s=""
        for ch in s:
            if ch.isalnum():
                formated_s +=ch
        
        left=0
        right=len(formated_s)-1
        while(left<right):
            if formated_s[left].lower() == formated_s[right].lower():
                left+=1
                right-=1
            else:
                return False
        return True



        
