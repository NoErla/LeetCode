"""
nvert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        """
        stack = [root]
        while stack:
            treenode = stack.pop()
            if treenode:
                treenode.left, treenode.right = treenode.right, treenode.left
                stack.append(treenode.left)
                stack.append(treenode.right)
        return root

