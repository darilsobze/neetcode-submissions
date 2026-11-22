from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def best(i):
            if i>=len(nums):
                return 0
            return max(best(i+1), nums[i]+best(i+2))
    
        return best(0)