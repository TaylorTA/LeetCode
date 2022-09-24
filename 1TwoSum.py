class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i, v in enumerate(nums):
            if v not in dic:
                dic[v] = [i]
            else:
                dic[v].append(i)
        
        for v in nums:
            if target - v in dic and target - v != v:
                return [dic[v][0], dic[target-v][0]]
            elif target - v in dic and target - v == v and len(dic[v])>1:
                return dic[v]
