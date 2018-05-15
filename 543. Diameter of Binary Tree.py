#Idea: Idea is the find deepest level count of the left tree and right tree. The sum of them is the diameter
# O(n) in time, O(1) in space
#AC in 56ms

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.best = 1
        self.depth(root)
        return self.best - 1
        
    def depth(self,root):
        if not root: return 0
        ansL = self.depth(root.left)
        ansR = self.depth(root.right)
        self.best = max(self.best, ansL + ansR + 1)
        return 1 + max(ansL, ansR) #increase the depth of this node by 1