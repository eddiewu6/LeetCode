


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest_path = 0
        self.longestUniPathHelper(root)
        return self.longest_path
        
    def longestUniPathHelper(self, root):
        if not root:
            return 0
        
        left_path = self.longestUniPathHelper(root.left)
        right_path = self.longestUniPathHelper(root.right)
        
        cur_left_path, cur_right_path = 0, 0
        
        if root.left and root.left.val == root.val:
            cur_left_path = left_path + 1
        if root.right and root.right.val == root.val:
            cur_right_path = right_path + 1
        
        self.longest_path = max(self.longest_path, cur_left_path + cur_right_path)
        #print(root.val,self.longest_path, cur_left_path, cur_right_path)
        return max(cur_left_path, cur_right_path)