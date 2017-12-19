"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

# Definition for singly-linked list.


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:

    @staticmethod
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        v = result
        carry_flag = False     #之前是否有进位

        while True:
            if l1 is None or l2 is None:
                z = l1.val if l1 else l2.val
                if carry_flag:
                    z = z + 1
                if z == 10:
                    v.next = ListNode(0)
                    carry_flag = True
                else:
                    v.next = ListNode(z)
                    carry_flag = False
            else:
                z = l1.val + l2.val + 1 if carry_flag else l1.val + l2.val
                if z < 10:
                    v.next = ListNode(z)
                    carry_flag = False
                else:
                    v.next = ListNode(z % 10)
                    carry_flag = True

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            v = v.next

            if l1 is None and l2 is None:
                if carry_flag:
                    v.next = ListNode(1)
                    break
                else:
                    break

        return result.next

        """       
        out = l1
        it = l1  # iterator
        ptr = l1
        total = 0
        while l2 is not None:
            if it is None:
                it = ListNode(0)
                ptr.next = it
            total += it.val + l2.val
            it.val = total % 10
            total //= 10
            ptr = it
            it = it.next
            l2 = l2.next
        while it is not None:
            ptr.next = it
            total += it.val
            it.val = total % 10
            total //= 10
            ptr = it
            it = it.next
        if total != 0:
            it = ListNode(total)
            ptr.next = it
        return out
        """

node1 = ListNode(9)
node1.next = ListNode(9)


node2 = ListNode(1)


Solution.addTwoNumbers(node1, node2)