class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = zip(efficiency, speed)
        engineers = sorted(engineers, key=lambda t:t[0], reverse=True)
        
        speedHeap = []
        speedSum = 0
        totalPerformance = 0
        
        for efficiency, speed in engineers:
            if len(speedHeap) > k-1:
                speedSum -= heapq.heappop(speedHeap)
            heapq.heappush(speedHeap, speed)
            speedSum += speed
            
            totalPerformance = max(totalPerformance, speedSum * efficiency)
        
        return totalPerformance % (10 ** 9 + 7)
