from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def best(i):
            if i>=n:
                return 1
            return best(i+1)+best(i+2)
        return best(1)