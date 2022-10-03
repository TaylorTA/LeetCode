class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        
        for i, n in enumerate(nums):
            if n!=0:
                nums[curr], nums[i] = nums[i], nums[curr]
                curr += 1
