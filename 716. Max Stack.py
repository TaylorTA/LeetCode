from sortedcontainers import SortedList

class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.pq = SortedList()
        self.curI = 0
        

    def push(self, x: int) -> None:
        self.stack.add((self.curI, x))
        self.pq.add((x, self.curI))
        self.curI += 1
        

    def pop(self) -> int:
        x = self.stack.pop()
        self.pq.remove(tuple(reversed(x)))
        return x[1]
        

    def top(self) -> int:
        return self.stack[-1][1]
        

    def peekMax(self) -> int:
        return self.pq[-1][0]
        

    def popMax(self) -> int:
        x = self.pq.pop()
        self.stack.remove(tuple(reversed(x)))
        return x[0]
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
