# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# wrong case 1 if all -1 using False, input{1} output false expected true
# attempted solution: add if leftheight == rightheight go to wrong case 2
# wrong case 2: when input{1#2#3} output wrong if I set all -1 using False
# solution:

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
        if leftTreeHeight - rightTreeHeight > 1 or rightTreeHeight - leftTreeHeight > 1:
            return -1
        else:
            return max(leftTreeHeight, rightTreeHeight) + 1
        
        