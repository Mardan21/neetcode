# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(cur, biggest_seen):
            nonlocal count
            if cur:
                count += 1 if cur.val >= biggest_seen else 0
                biggest_seen = max(biggest_seen, cur.val)
            else:
                return
            dfs(cur.left, biggest_seen)
            dfs(cur.right, biggest_seen)

        dfs(root, float('-inf'))
        return count
        