'''Given the root of a binary tree, return the average value of the nodes 
on each level in the form of an array. Answers within 10-5 of the actual 
answer will be accepted.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def get_arr(root):
            levels = []
            if not root:
                return levels

            def helper(node, level):
                if len(levels) == level:
                    levels.append([])
                
                levels[level].append(node.val)
                if node.left:
                    helper(node.left, level+1)
                if node.right:
                    helper(node.right, level+1)

            helper(root, 0)
            return levels
        arr = get_arr(root)
        print(arr)
        ans = [sum(x)/len(x) for x in arr]
        return ans
