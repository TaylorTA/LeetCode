class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        arr = [head]
        curr = head.next
        while curr:
            arr.append(curr)
            curr = curr.next
        
        return arr[len(arr)//2]
