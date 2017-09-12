'''
Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not lists:
            return None
        head = ListNode(None)
        prev = head
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize():
            prev.next = q.get()[1]
            prev = prev.next
            if prev.next:
                q.put((prev.next.val, prev.next))
        return head.next

l1 =ListNode(0)
l1.next = ListNode(2)
l1.next.next = ListNode(5)
# l2 = None
# l3 = ListNode(-1)
s = Solution()
l = s.mergeKLists([l1])
if not l: print(l)
while l:
    print(l.val)
    l = l.next