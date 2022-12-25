class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(queries)):
            l = queries[i]
            s = 0
            n = 0
            while n<len(nums) and (s+nums[n])<=l:
                s += nums[n]
                n += 1
            queries[i] = n
            #print(queries)
        return queries
