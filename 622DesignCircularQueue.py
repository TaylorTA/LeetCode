class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.first = None
        self.size = 0
        self.maxSize = k
        

    def enQueue(self, value: int) -> bool:
        if self.size == self.maxSize:
            return False
        else:
            if not self.first:
                self.first = ListNode(value)
                self.first.next = self.first
                self.size += 1
            else:
                f = self.first
                curr = f
                while(curr.next != f):
                    curr = curr.next
                curr.next = ListNode(value, self.first)
                self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        elif self.size == 1:
            self.size -=1
            self.first = None
            return True
        else:
            self.size -= 1
            f = self.first
            curr = self.first
            while(curr.next != f):
                curr = curr.next
            curr.next = f.next
            self.first = f.next
            return True
            

    def Front(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.first.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        else:
            f = self.first
            curr = self.first
            while(curr.next != f):
                curr = curr.next
            return curr.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxSize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
