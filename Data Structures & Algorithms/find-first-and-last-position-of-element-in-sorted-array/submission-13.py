class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums,target,True)
        right= self.binary_search(nums,target,False)
        return [left, right]

    def binary_search(self, nums:List[int], target: int, leftBias: bool) -> List[int]:
        l=0
        r=len(nums)-1
        result=-1
        while(l<=r):
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                result=mid
                if leftBias:
                    r=mid-1
                else:
                    l=mid+1
            
        return result







