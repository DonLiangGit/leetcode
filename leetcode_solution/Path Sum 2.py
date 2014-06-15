# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Memory Limit Exceeded: Solution/append wrong list,arguement is wrong
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
    	if root == None:
    		return []
    	Solution.sum = sum
    	Solution.result = []
    	self.subpathSum(root,[root.val],root.val)
    	return Solution.result

    def subpathSum(self, node, temList, temSum):
    	if node.left == None and node.right == None:
    		if temSum == Solution.sum:
    			Solution.result.append(temList)
    		return
    	if node.left != None:
    		self.subpathSum (node.left, temList+[node.left.val], temSum+node.left.val)
    	if node.right != None:
    		self.subpathSum (node.right, temList+[node.right.val], temSum+node.right.val)