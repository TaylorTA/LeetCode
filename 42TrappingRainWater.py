class Solution:
    def trap(self, height: List[int]) -> int:
        maxRain = 0
        leftMax = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i-1])
        
        rightMax = [0 for _ in range(len(height))]
        for i in range(len(height)-2,-1,-1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
        
        for i in range(1,len(height)-1):
            rain = min(leftMax[i], rightMax[i]) - height[i]
            maxRain += max(0, rain)
        
        return maxRain
