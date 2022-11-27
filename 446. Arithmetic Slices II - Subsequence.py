class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [collections.defaultdict(int) for _ in range(len(nums))]
        c = 0
        for i in range(len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]
                c += dp[j][d]
                dp[i][d]+= dp[j][d] + 1
        return c
