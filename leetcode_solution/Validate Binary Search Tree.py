# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# wrong answer: Input:	{1,#,1} Output:	true Expected:	false / arguement is wrong at the last return.

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if root == None:
        	return True
        else:
        	return self.isValidSubBST(root, -2**31, 2**31-1)

    def isValidSubBST(self, root, min, max):
    	if root == None:
    		return True
    	else:
    		return root.val > min and root.val < max and self.isValidSubBST(root.left, min, root.val) and self.isValidSubBST(root.right, root.val, max)