class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :param head:
        :return:
        """
        length, temp = 0, head
        while temp != None:
            length += 1
            temp = temp.next
        new_node = head
        for _ in range(length // 2):
            new_node = new_node.next
        return new_node


def middleNode(head):
    slow, fast = head, head
    while slow.next is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
