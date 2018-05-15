#Solution: transverse the tree and get the minimum absolute value of root.val - target
#O(n) in time, O(1) in space
#AC in 68ms


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.node = None
        self.transverse(root,target,sys.maxsize)
        return self.node
        
        
    def transverse(self,root,target,minNode):
        if root == None:
            return sys.maxsize
        else:
            if minNode > abs(root.val-target):
                minNode = abs(root.val-target)
                self.node = root.val
            return min(minNode,self.transverse(root.left,target,minNode),self.transverse(root.right,target,minNode))
        