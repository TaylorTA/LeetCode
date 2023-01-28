from sortedcontainers import SortedList
class SummaryRanges:

    def __init__(self):
        self.list = SortedList()
        

    def addNum(self, value: int) -> None:
        self.list.add(value)


    def getIntervals(self) -> List[List[int]]:
        ans = []
        left, right = -1, -1
        for n in self.list:
            if left<0:
                left, right = n, n
            elif n == right+1 or n == right:
                right = n
            else:
                ans.append([left,right])
                left, right = n, n
        ans.append([left,right])
        return ans
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
