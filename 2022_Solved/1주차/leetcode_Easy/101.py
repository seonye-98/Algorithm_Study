'''
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root.left, root.right)

        
        
    def check(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        
        if left.val == right.val:
            return self.check(left.right, right.left) and self.check(left.left, right.right)
        
        else:
            return False

