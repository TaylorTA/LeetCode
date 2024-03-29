class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = [0 for _ in range(len(nums))]
        
        if len(nums) > 0:
            sums[0] = nums[0]
        
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]
        
        return sums
