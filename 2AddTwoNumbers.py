# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = None
        curr3 = l3
        add1 = 0
        
        while l1 and l2:
            s = l1.val + l2.val + add1
            add1 = 0
            if s > 9:
                s -= 10
                add1 = 1
            newNode = ListNode(s,None)
            if not l3:
                l3 = newNode
                curr3 = newNode
            else:
                curr3.next = newNode
                curr3 = curr3.next
            
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            print(l1)
            print(l3)
            curr3.next = l1
            s = l1.val + add1
            while (s > 9 or add1) and l1:
                s = l1.val + add1
                if s >= 10:
                    l1.val = s - 10
                    add1 = 1
                else:
                    l1.val = s
                    add1 = 0
                curr3 = l1
                l1 = l1.next

        elif l2:
            curr3.next = l2
            s = l2.val + add1
            while (s > 9 or add1) and l2:
                s = l2.val + add1
                if s >= 10:
                    l2.val = s - 10
                    add1 = 1
                else:
                    l2.val = s
                    add1 = 0
                curr3 = l2
                l2 = l2.next
                
        if add1:
            curr3.next = ListNode(1,None)
        
        return l3
