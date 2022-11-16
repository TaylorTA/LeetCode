# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        h = n
        m = n//2
        c = guess(m)
        while c != 0:
            if c == -1:
                h = m-1
            else:
                l = m+1
            m = (l+h)//2
            c = guess(m)
        return m
