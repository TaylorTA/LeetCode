class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = len(nums)-1
        maxs = -1

        while left < right:
            sumc = nums[left] + nums[right]
            if sumc < k:
                maxs = max(sumc, maxs)
                left += 1
            else:
                right -= 1
        
        return maxs
