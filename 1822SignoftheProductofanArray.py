class Solution:
    def arraySign(self, nums: List[int]) -> int:
        numn = 0
        
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                numn += 1
        
        if numn % 2 == 0:
            return 1
        else:
            return -1
