class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast: # 相遇
                break
        if not fast or not fast.next: # 没有环
            return None
        tmp = head # 增加一个起点根slow一起遍历
        while slow and tmp != slow:
            tmp = tmp.next
            slow = slow.next
        return slow