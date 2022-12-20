class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def rob1(nums: List[int]) -> int:
            if not nums:
                return 0

            m = 0
            dp = [0 for _ in range(len(nums)+1)]
            dp[-2] = nums[-1]

            for i in range(len(nums)-2, -1, -1):
                dp[i] = max(nums[i]+dp[i+2], dp[i+1])
        
            return dp[0]
        return max(rob1(nums[:-1]), rob1(nums[1:]))
