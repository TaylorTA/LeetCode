# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        if head is None:
            return head
        else:
            newHead = ListNode(head.val)
            head = head.next
            while(head):
                newHead = ListNode(head.val, newHead)
                head = head.next
        
        return newHead
