from collections import deque

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = deque()
        ts = deque()
        for c in s:
            if c != "#":
                ss.append(c)
            elif ss:
                ss.pop()
        for c in t:
            if c!= "#":
                ts.append(c)
            elif ts:
                ts.pop()
        return ss == ts
