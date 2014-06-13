# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# UnboundLocalError: local variable 'sum' referenced before assignment
# Solution:

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
    	if root == None:
    		return 0
    	if root.left == None and root.right == None:
    		return root.val
    	Solution.sum = 0
    	if root.left != None:self.getSum(root.left, root.val)
    	if root.right != None:self.getSum(root.right, root.val)
    	
    	return Solution.sum

    def getSum(self, node, parenetValue):
    	if node == None:
    		return
    	if node.left == None and node.right == None:
    		Solution.sum += node.val + parenetValue*10

    	self.getSum(node.left, parenetValue*10 + node.val)
    	self.getSum(node.right, parenetValue*10 + node.val)

    	return
