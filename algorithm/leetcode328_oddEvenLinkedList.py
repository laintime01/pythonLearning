# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head

        odd, even = head, head.next
        now_odd, now_even = odd, even

        while now_even.next:
            now_odd.next = now_even.next
            now_odd = now_odd.next
            now_even.next = now_odd.next
            if now_even.next:
                now_even = now_even.next
        now_odd.next = even
        return odd