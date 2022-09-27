class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums2)
        inter = []
        for num in nums1:
            if num in count:
                inter.append(num)
                count[num] -= 1
                if count[num] == 0:
                    count.pop(num)
        
        return inter
