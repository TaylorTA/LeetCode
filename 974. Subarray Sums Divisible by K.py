class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #    [4,5,0,-2,-3,1]
        #     ~~~~~~~~
        #     ~~~~~~~~~~~~~
        #             ~~~~~
        # [0, 4,9,9, 7, 4,5]
        #            ^    ^

        mod = [0] * k 
        pmod = 0
        ans = 0
        mod[0] = 1
        for n in nums:
            pmod = (pmod + n)%k 
            ans += mod[pmod]
            mod[pmod] += 1
        return ans
