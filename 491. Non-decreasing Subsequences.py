class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        suba = []

        def b(i):
            #print(suba)
            if i == len(nums):
                if len(suba)>=2:
                    ans.add(tuple(suba))
                return
            
            if len(suba) == 0 or suba[-1] <= nums[i]:
                suba.append(nums[i])
                b(i+1)
                suba.pop()
            b(i+1)
        
        b(0)
        return ans
