class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        best=r
        while l<=r:
            mid=(l+r)//2
            total_duration=0
            for pile in piles:
                current_duration=math.ceil(pile/mid)
                total_duration+=current_duration
            if total_duration > h:
                l=mid+1
            else:
                best = mid
                r=mid-1
        return best