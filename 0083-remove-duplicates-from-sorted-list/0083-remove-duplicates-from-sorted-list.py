class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        
        while current:
            while current.next and current.val == current.next.val:
                current.next = current.next.next  # skip duplicate
            current = current.next
        
        return head