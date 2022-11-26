class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        js = sorted(zip(startTime, endTime, profit))
        dp = [0] * (len(js)+1)
        st = [j[0] for j in js]

        for i in range(len(js)-1, -1, -1):
            nj = bisect.bisect_left(st, js[i][1])
            dp[i] = max(dp[i+1], js[i][2]+dp[nj])
        
        return dp[0]
