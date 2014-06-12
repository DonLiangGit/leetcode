# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
    	# root is a tree node
    	# and the self means the tree itself
        if root == None:
            return 0
        if root.left == None:
            return self.minDepth(root.right) + 1
        if root.right == None:
            return self.minDepth(root.left) + 1
    	# to compare the depth of left tree and right tree;
    	# we need to use built-in function min()
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        return min(leftDepth, rightDepth) + 1