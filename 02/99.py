'''
Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = []
        x = y = prev = None
        while root or len(stack):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and prev.val >= root.val:
                if not x:
                    x = prev
                if x:
                    y = root
            prev = root
            root = root.right

        x.val, y.val = y.val, x.val



root = TreeNode(0)
root.left = TreeNode(1)
s = Solution()
s.recoverTree(root)

stack = []
while root or len(stack):
    while root:
        stack.append(root)
        root = root.left
    root = stack.pop()
    print(root.val)
    root = root.right