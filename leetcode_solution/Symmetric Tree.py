# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Runtime error: global name is not defined/ because i don't mention, the source for arguement, need to declare self.method().
# Runtime error: Root got its left and right children, instead of self!
# Runtime error: arguement amount/change the function isSymBoth(self,a1,a2)
# Runtime error: attribute error/

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
    	# case1: whether the tree is empty
        if root == None:
        	return True
        return self.isSymBoth(root.left,root.right)


    def isSymBoth(self,leftNode,rightNode):
    	# case2: judge the Null condition for two children;
    	if leftNode == None:
    		return rightNode == None
    	elif rightNode == None:
    		return False
    	# judge the current Node value
    	if leftNode.val != rightNode.val:
    		return False
        
        # important!
    	if (not self.isSymBoth(leftNode.left, rightNode.right)):
    		return False
    	elif (not self.isSymBoth(leftNode.right, rightNode.left)):
    		return False
    
    	return True
