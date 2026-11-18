class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l=0
        r=1
        biggest=1
        length=1
        map={s[l]:l}
        while(l<r and r<len(s)):
            if s[r] not in map:
                map[s[r]]=r
                #length+=1
            else: 
                l=max(l,map[s[r]]+1)
                map[s[r]]=r
                #length = r-l+1
            biggest= max(biggest, r-l+1)
            r+=1
            
        return biggest
                