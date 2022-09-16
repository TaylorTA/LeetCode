class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        dp = [[0] * (len(multipliers)+1) for _ in range(len(multipliers)+1)]
        
        for mult in range(len(multipliers)-1, -1, -1):
            for left in range(mult, -1, -1):
                dp[mult][left] = max(dp[mult+1][left+1] + nums[left]*multipliers[mult], dp[mult+1][left] + nums[len(nums) - 1 - mult + left]*multipliers[mult])
        
        return dp[0][0]
