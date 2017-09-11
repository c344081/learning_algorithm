'''
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        minDepth = 0
        while len(queue):
            count = len(queue)
            while count > 0:
                node = queue.popleft()
                if not node.left and not node.right:
                    return minDepth + 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                count -= 1
            minDepth += 1
        return minDepth

root = TreeNode(1)
root.left = TreeNode(2)
s = Solution()
depth = s.minDepth(root)
print(depth)