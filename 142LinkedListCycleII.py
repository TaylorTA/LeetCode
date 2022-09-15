# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
    
        if not head.next:
            return None
            
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break;
        
        if not fast or not slow or fast != slow:
            return None
        
        intersect = head
        
        while intersect != slow:
            intersect = intersect.next
            slow = slow.next
            
        return intersect
