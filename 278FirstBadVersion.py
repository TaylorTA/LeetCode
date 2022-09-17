# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 0
        hi = n
        mid = (lo+hi)//2
        
        while(lo<hi):
            if isBadVersion(mid) is False:
                lo = mid+1
            else:
                hi = mid
            mid = (lo+hi)//2
        
        return lo
