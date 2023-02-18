#ListNode
import math


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        if not head or not head.next:
            return head

        # number of node
        count, node = 0, head

        while node:
            count +=1
            node = node.next

        # shadow node res
        res = ListNode(0)
        # point res to head
        res.next = head
        tail, _next = None, None

        # sort
        for i in range(math.ceil((math.log(count, 2)))):
            # elements numbers need to sort
            nums = 2**i
            # tail means tail node that is sorted
            tail = res
            # make _next head, means the beginning of next sort
            _next = res.next
            while _next:
                # left is first and right is second
                left = _next
                right = self._depart(left, nums -1)
                _next = self._depart(right, nums-1)

                sortedhead, sortedtail = self._merge(left, right)
                tail.next = sortedhead
                tail = sortedtail
            temp = res
            res= res.next
            del temp
            return res

    def _depart(self, head, steps):
        node = head
        while node and steps:
            node = node.next
            steps -= 1
        res = node.next if node else None

        if node: node.next = None
        return res

    def _merge(self, left, right):
        node = ListNode(0)
        tail = node

        while left and right:
            if left.val > right.val:left,right = right, left

            tail.next = left
            left = left.next
            tail = tail.next

        if left:tail.next = left
        if right:tail.next = right
        res, tail = node.next, node
        while tail.next:
            tail = tail.next
        del node
        return res, tail