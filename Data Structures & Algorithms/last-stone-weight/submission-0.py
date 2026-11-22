class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i, stone in enumerate(stones):
            heapq.heappush(heap,-stone)
        last=0
        while len(heap)>1:
            first= heapq.heappop(heap)
            second = heapq.heappop(heap)
            if second > first:
                heapq.heappush(heap, first-second)
        heap.append(0)
        return abs(heap[0])
