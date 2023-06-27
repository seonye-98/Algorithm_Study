'''
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

sol1) 재귀 : 젤 느림
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None 
        right = self.invertTree(root.right) 
        left = self.invertTree(root.left) 
        root.left = right 
        root.right = left 
        return root

sol2) BFS
class Solution:
    def invertTree(self, root):
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            # 부모 노드로부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
 
                queue.append(node.left)
                queue.append(node.right)
                
        return root

sol3) DFS
'''
class Solution:
    def invertTree(self, root):
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            # 부모 노드로부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
 
                stack.append(node.left)
                stack.append(node.right)
                
        return root


