# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(-1, head)

        e = d
        c = 0
        while(e.next != None):
            e = e.next
            c += 1
        
        cur = d.next
        pre = d
        i = 1
        while(cur != None):
            if i>c:
                break
            if i % 2 == 0:
                if i != c or c != 2:
                    pre.next = cur.next
                e.next = cur
                cur.next = None
                e = cur
                cur = pre.next
            else:
                pre = cur
                cur = cur.next
            i += 1

        return d.next
