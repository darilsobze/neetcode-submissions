class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        if nums[left]<nums[right]:
            return nums[left]
        else:
            while (left<right):
                left= left+1
                right = right-1
                if nums[left]<=nums[right]:
                    if nums[left]<nums[left-1]:
                        return nums[left]
                    return nums[right+1]
        return nums[left]

