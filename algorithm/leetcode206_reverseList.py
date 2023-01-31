class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        new_tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_tail
