# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNodeFromList(self, head, n):
        """
        :param head: ListNode
        :param n: int
        :return: ListNode
        """
        p = head
        stack = []
        while p:
            stack.append(p)
            p = p.next
        for i in range(n):
            stack.pop()
        if len(stack) == 0:
            return head.next

        p = stack.pop()
        p.next = p.next.next
        return head
