class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        times ={}
        for i in range(len(nums)):
            times[nums[i]] = times.get(nums[i], 0) + 1
        result = []
        while k>0:
            top=0
            for num in times:
                if times[num] > top:
                    top= times[num]
                    number_top = num
            result = result + [number_top]
            times[number_top]=0
            k-=1
        return result
        