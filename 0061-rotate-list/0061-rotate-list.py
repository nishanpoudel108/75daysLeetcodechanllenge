class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # make circular
        tail.next = head

        # find new tail
        steps = length - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next

        # new head
        new_head = new_tail.next
        new_tail.next = None

        return new_head