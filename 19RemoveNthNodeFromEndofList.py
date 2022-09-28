# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        
        if n == 1 and not head.next:
            return None
        
        for i in range(n):
            first = first.next
        
        if not first:
            head = head.next
            return head
        
        while first.next:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return head
