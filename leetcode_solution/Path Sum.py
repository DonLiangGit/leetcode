# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
    	# case 1: if the tree is empty, return False
        if root == None:
        	return False
        # case 2: if the tree only has one root node, compare the valut to target
        if root.left == None and root.right == None:
            # return whether the root.val is equal to sum, returns a boolean value.
        	return root.val == sum
        # case 3: otherwise, return OR
        # Called Logical OR Operator. If any of the two operands are non zero then then condition becomes true.
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

