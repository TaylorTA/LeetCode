class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num3 = defaultdict(int)
        
        con1 = len(nums1)%2
        con2 = len(nums2)%2
        
        op = 0
        if con1:
            op = op ^ reduce(lambda x, y: x ^ y, nums2)
        if con2:
            op = op ^ reduce(lambda x, y: x ^ y, nums1)
        
        return op
