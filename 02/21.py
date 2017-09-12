'''
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        node1 = l1
        node2 = l2
        root = ListNode(None)
        prev = root
        while node1 and node2:
            if node1.val >= node2.val:
                prev.next = node2
                node2 = node2.next
            else:
                prev.next = node1
                node1 = node1.next
            prev = prev.next

        if node1:
            prev.next = node1
        elif node2:
            prev.next = node2

        return root.next

l1 = ListNode(2)
l2 = ListNode(1)
s = Solution()
l = s.mergeTwoLists(l1, l2)
while l:
    print(l.val)
    l = l.next