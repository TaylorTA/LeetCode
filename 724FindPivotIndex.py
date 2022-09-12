class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        listSum = sum(nums)
        
        leftSum = 0
        for i in range(len(nums)):
            if leftSum == (listSum - nums[i])/2:
                return i
            leftSum += nums[i]
        
        return -1
