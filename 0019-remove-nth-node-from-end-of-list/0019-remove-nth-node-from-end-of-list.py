class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both until fast reaches end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Remove nth node
        slow.next = slow.next.next
        
        return dummy.next