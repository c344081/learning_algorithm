'''
Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        runner = head
        walker = head
        prev = None
        while runner and runner.next:
            runner = runner.next.next
            prev = walker
            walker = walker.next
        root = TreeNode(walker.val)
        if prev:
            prev.next = None
        else:
            head = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(walker.next)

        return root

