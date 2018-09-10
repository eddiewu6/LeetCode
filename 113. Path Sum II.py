# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(root,sum,[])
        return self.res



    def dfs(self, root, total, pre):
        if not root:
            return []
        if not root.left and not root.right and total == root.val:
            pre.append(root.val)
            self.res.append(pre)
        if root.left:
            self.dfs(root.left, total - root.val, pre + [root.val])
        if root.right:
            self.dfs(root.right, total - root.val, pre + [root.val])
