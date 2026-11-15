class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first=0
        second=1
        while first<second:
            if numbers[first] + numbers[second] == target:
                break
            elif numbers[first] + numbers[second] < target:
                first+=1
                second+=1
            else:
                first-=1
        return [first+1, second+1]