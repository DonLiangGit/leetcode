# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def preOrder(self, root, level, result):
    	if root != None:
    		if len(result) < level+1:
    			result.append([])
    		result[level].append(root.val)
    		self.preOrder(root.left, level+1, result)
    		self.preOrder(root.right, level+1, result)
    def levelOrder(self, root):
    	result = []
    	self.preOrder(root, 0, result)
    	return result
        