# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# runtime error: last input is [1,3]

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0:
            return None
        return self.buildTree(num, 0, len(num)-1)

    def buildTree(self, num, first, last):
    	# beware of this condition, if input is [1,3]
    	# it will not run because could not get the num value
    	if first > last:
    		return None
    	mid = (first + last) / 2
    	root = TreeNode(num[mid])

    	root.left = self.buildTree(num, first, mid-1)
    	root.right = self.buildTree (num, mid+1, last)

    	return root