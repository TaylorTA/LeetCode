class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dic = [set() for _ in range(26)]
        for w in ideas:
            dic[ord(w[0])-ord('a')].add(w[1:])
        
        ans = 0
        for i in range(25):
            for j in range(i+1, 26):
                c = len(dic[i] & dic[j])
                ans += (len(dic[i])-c) * (len(dic[j])-c) * 2
        return ans
