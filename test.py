class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.cams = 0
        ans = self.dfs(root)
        return self.cams + 1 if ans == 0 else self.cams

    #1 -> covered by camera
    #2 -> node with has camera
    #3 -> not covered by camera
    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 1
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left == 0 or right == 0:
            self.cams += 1
            return 2
        elif left == 2 or right == 2:
            return 1
        else:
            return 0


sol = Solution()
root = TreeNode(0)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(0)

print(sol.minCameraCover(root))