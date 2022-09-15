class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) == 0 or len(changed)%2 == 1:
            return []
        
        changed.sort()
        
        original = []
        nums = {}
        
        for num in changed:
            if num not in nums:
                nums[num] = 1
            else:
                nums[num] = nums[num]+1
        
        for num in changed:
            # print(nums)
            if nums[num] >= 1:
                if (num*2) in nums and nums[(num*2)] >= 1:
                    # print(num)
                    nums[num] -= 1
                    nums[num*2] -= 1
                    original.append(num)
                else:
                    return []
        
        return original
