class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        randomMap = {}

        curr = head
        while curr:
            randomMap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                randomMap[curr].next = randomMap[curr.next]
            if curr.random:
                randomMap[curr].random = randomMap[curr.random]
            curr = curr.next

        return randomMap[head]