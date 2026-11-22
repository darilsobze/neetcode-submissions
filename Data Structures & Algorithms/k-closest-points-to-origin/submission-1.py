class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            heapq.heappush(heap, ( -(pow(point[0],2) + pow(point[1],2)), point))
            if len(heap)>k:
                heapq.heappop(heap)
        return [point for i, point in heap]
