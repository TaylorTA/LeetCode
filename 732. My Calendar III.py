from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.dic = SortedDict()

    def book(self, start: int, end: int) -> int:
        maxb = 0
        
        self.dic[start] = self.dic.get(start, 0) + 1
        self.dic[end] = self.dic.get(end, 0) - 1
        
        curr = 0
        for t in self.dic.values():
            curr += t
            maxb = max(maxb, curr)
        
        return maxb


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
