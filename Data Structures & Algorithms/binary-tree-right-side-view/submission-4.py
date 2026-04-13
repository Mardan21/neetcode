# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, rightView = [], []

        # O(n) -> n = # of nodes in tree
        def bfs(curr, height):
            if not curr:
                return

            nonlocal res
            if len(res) > height:
                res[height].append(curr.val)
            else:
                res.append([curr.val])
            
            bfs(curr.left, height + 1)
            bfs(curr.right, height + 1)

        bfs(root, 0)

        # O(h) -> h = height of the tree
        for level in res:
            rightView.append(level[-1])

        return rightView
