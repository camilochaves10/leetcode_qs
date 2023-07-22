'''Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []
        if root is None:
            return True

        def dfsl(node):
            if node is None:
                left.append('none')
                return
            left.append(node.val)
            dfsl(node.left)
            dfsl(node.right)
        
        def dfsr(node):
            if node is None:
                right.append('none')
                return
            right.append(node.val)
            dfsr(node.right)
            dfsr(node.left)
            
        dfsl(root.left)
        dfsr(root.right)
        print(left, right)
        return left==right

