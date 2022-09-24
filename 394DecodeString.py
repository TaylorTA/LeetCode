from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        op = ""
        k = 0
        toAdd = ""
        ks = deque()
        ss = deque()
        curr = ""

        for c in s:
            if c.isnumeric():
                k = k*10 + int(c)
            elif c == "[":
                ks.append(k)
                k = 0
                ss.append(curr)
                curr = ""
            elif c == "]":
                prev = ss.pop()
                for i in range(ks.pop()):
                    prev += curr
                curr = prev
            else:
                curr += c
                 
        return curr
