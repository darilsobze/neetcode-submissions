class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            difference= target-nums[i]
            if difference in dic:
                break
            else: 
                dic[nums[i]]=i
                continue
        return [dic[difference], i]


        