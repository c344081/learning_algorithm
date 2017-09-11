'''
Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS 深度优先, 前序遍历
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [root]
        values = [1]
        maxNum = 0
        while len(stack):
            node = stack.pop()
            tmp = values.pop()
            maxNum = max(tmp, maxNum)
            if node.right:
                stack.append(node.right)
                values.append(tmp + 1)
            if node.left:
                stack.append(node.left)
                values.append(tmp + 1)
        return maxNum

# BFS 广度优先
from collections import deque
class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = deque()
        maxNum = 0
        queue.append(root)
        while len(queue):
            count = len(queue)
            while count > 0:
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                count -= 1
            maxNum += 1
        return maxNum

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
s = Solution2()
num = s.maxDepth(root)
print(num)