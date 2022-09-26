class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = set()
        
        for n in nums:
            if n in sets:
                return True
            else:
                sets.add(n)
        
        return False
