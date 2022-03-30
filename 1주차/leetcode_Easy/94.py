'''
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

inorder traversal(중위순회)
왼쪽 끝까지 내려간 이후 루트를 방문하고 오른쪽 자식노드로 이동하여 순회를 계속
'''
class Solution:
    def inorderTraversal(self, root):
        answer = []
        self.traversal(root, answer)
        return answer
    
    def traversal(self, node, result):
        if node:
            self.traversal(node.left, result)
            result.append(node.val)
            self.traversal(node.right, result)