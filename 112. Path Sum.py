#
#O(n) in time, O(1) in space
#AC in 77ms



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        else:
            if root.val == sum and root.left == None and root.right == None:#Insure it is the leaf node
                return True
            else:
                return self.hasPathSum(root.left,(sum-root.val)) or self.hasPathSum(root.right,(sum-root.val))