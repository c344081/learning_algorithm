'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lastNode = None
        head = None
        while(l1 or l2):
            if not l1:
                value = l2.val
            elif not l2:
                value = l1.val
            else:
                value  = l1.val + l2.val
            if not lastNode:
                lastNode = ListNode(value)
                head = lastNode
            else:
                if lastNode.val >= 10:
                    lastNode.val -= 10
                    value += 1
                lastNode.next = ListNode(value)
                lastNode = lastNode.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if not l1 and not l2:
                if value >= 10:
                    lastNode.val -= 10
                    lastNode.next = ListNode(1)
        return head

l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

l2 = ListNode(0)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

solution = Solution()
l3 = solution.addTwoNumbers(l1, l2)

l = l3
while l:
    print("val:%d" % l.val)
    l = l.next