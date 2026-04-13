# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightView = []

        # O(n) -> n = # of nodes in tree
        def dfs(curr, depth):
            if not curr:
                return

            if depth == len(rightView):
                rightView.append(curr.val)
            
            # recurse on right first for rightmost in rightView[]
            dfs(curr.right, depth + 1)
            dfs(curr.left, depth + 1)

        dfs(root, 0)

        return rightView
