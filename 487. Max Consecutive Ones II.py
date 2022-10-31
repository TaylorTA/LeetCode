class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr1 = 0
        curr0 = 0
        left = 0
        max1 = 0
        
        for i, n in enumerate(nums):
            if n == 1:
                curr1 += 1
            else:
                curr0 += 1
            
            if curr0 == 2:
                max1 = max(curr1, max1)
                while(nums[left] != 0):
                    left += 1
                    curr1 -= 1
                left += 1
                curr0 -= 1
            
        max1 = max(curr1, max1)
        
        return max1+curr0
