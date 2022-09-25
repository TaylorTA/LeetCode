class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        diff = 0
        
        while(stones):
            stone1 = -heapq.heappop(stones)
            stone2 = 0
            if stones:
                stone2 = -heapq.heappop(stones)
            diff = abs(stone1 - stone2)
            if stones:
                heapq.heappush(stones, -diff)
        
        return diff
