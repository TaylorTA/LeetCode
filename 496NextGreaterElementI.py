class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = defaultdict(int)
        
        for num in nums2:
            while len(stack)>0 and stack[-1] < num:
                dic[stack.pop()] = num
            stack.append(num)
        
        for i in range(len(nums1)):
            if nums1[i] in dic:
                nums1[i] = dic[nums1[i]]
            else:
                nums1[i] = -1
        
        return nums1
