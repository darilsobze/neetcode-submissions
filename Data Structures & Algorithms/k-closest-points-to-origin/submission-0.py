class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        result=[]
        for point in points:
            heapq.heappush(heap, ( -(pow(point[0],2) + pow(point[1],2)), point))
            if len(heap)>k:
                heapq.heappop(heap)
        for i,point in heap:
            result.append(point)
        return result
