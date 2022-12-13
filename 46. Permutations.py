class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bk(f):
            if f == len(nums):
                op.append(nums[:])
            for i in range(f, len(nums)):
                nums[f], nums[i] = nums[i], nums[f]
                bk(f+1)
                nums[f], nums[i] = nums[i], nums[f]
        op = []
        bk(0)
        return op
