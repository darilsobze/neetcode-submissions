class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best=0
        for start in nums_set:
            if start-1 in nums_set:
                continue
            end=start+1
            while end in nums_set:
                end+=1
            best= max(best, end-start)
        return best
