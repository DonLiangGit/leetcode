# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None:
            return True
            
        leftHeight = self.treeHeight(root.left)
        rightHeight = self.treeHeight(root.right)
        if leftHeight == -1:
            return False
        if rightHeight == -1:
            return False
        if leftHeight - rightHeight > 1 or rightHeight - leftHeight > 1:
            return False
        else:
            return True
    
    def treeHeight(self, root):
        if root == None:
            return 0
        leftTreeHeight = self.treeHeight(root.left)
        rightTreeHeight = self.treeHeight(root.right)
        if leftTreeHeight == -1:
            return -1
        if rightTreeHeight == -1:
            return -1
        # every time to calculate the height need to compare the tree if it is not balanced,
        # return -1 immediately.
        if leftTreeHeight - rightTreeHeight > 1 or rightTreeHeight - leftTreeHeight > 1:
            return -1
        else:
            return max(leftTreeHeight, rightTreeHeight) + 1
        
        