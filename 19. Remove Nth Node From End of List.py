"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return []
        list = []
        while head is not None:
            list.append(head)
            head = head.next
        if n == len(list):
            return list[1]
        if list[-n].next is None:
            list[-(n+1)].next = None
        else:
            list[-(n + 1)].next = list[-(n - 1)]
        return list[0]

s = Solution()
a = ListNode(1)
a.next = ListNode(2)
print(s.removeNthFromEnd(a, 2).val)