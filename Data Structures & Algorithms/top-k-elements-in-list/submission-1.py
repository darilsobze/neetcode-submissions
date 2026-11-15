class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        times ={}
        for i in range(len(nums)):
            times[nums[i]] = times.get(nums[i], 0) + 1
        arr = []
        for num , count in times.items():
            arr.append([count,num])
        arr.sort()

        result=[]
        while k>0:
            result.append(arr.pop()[1])
            k-=1
        return result
        