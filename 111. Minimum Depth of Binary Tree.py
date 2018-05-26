#Solution1 DFS find the depth of minimum, check whether it is the leaf node
#O(n) in time, O(1) in space
#AC in 69ms

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.dfs(root)
        
    def dfs(self,root):
        if root == None:
            return 0
        depthLeft = self.minDepth(root.left)
        depthRight = self.minDepth(root.right)
        if depthLeft > 0 or depthRight > 0:
            if depthLeft == 0:
                return depthRight + 1
            if depthRight == 0:
                return depthLeft + 1
        return min(depthLeft,depthRight) + 1

#Solution2
#
#
def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    self.res=sys.maxsize
    self.helper(root,0)
    return self.res
    
def helper(self,root,depth):
        if root.left:
            self.helper(root.left,depth+1)
        if root.right:
            self.helper(root.right,depth+1)
        if not root.left and not root.right :
            self.res=min(self.res,depth+1)
