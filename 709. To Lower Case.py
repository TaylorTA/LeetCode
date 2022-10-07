class Solution:
    def toLowerCase(self, s: str) -> str:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        dic = dict(zip(upper, lower))
        return "".join(dic[x] if x in dic else x for x in s)
