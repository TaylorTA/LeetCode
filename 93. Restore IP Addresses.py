class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = set()
        temp = []
        def bt(pos):
            if pos >= len(s):
                if len(temp) == 4:
                    ans.add(".".join(temp))
                return
            for i in range(1,4):
                t = s[pos:pos+i]
                if len(t)>1 and (t[0] == '0' or int(t)>255):
                    continue
                temp.append(t)
                bt(pos+i)
                temp.pop()
        bt(0)
        return ans
