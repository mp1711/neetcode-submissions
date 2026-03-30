class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # find the kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # reverse this group
            prev = group_next
            curr = group_prev.next

            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # connect with previous part
            tmp = group_prev.next
            group_prev.next = prev
            group_prev = tmp
