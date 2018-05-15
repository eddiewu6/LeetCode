#inorder transverse to put all the element in a list, and find the minimum distance
#O() in time, O(n) in space
#AC in 40ms

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = sys.maxsize
        s = []
        self.transverse(root,s)
        for i in range(1,len(s)):
            if abs(s[i]-s[i-1]) < res:
                res = abs(s[i]-s[i-1])
        return res
        
    def transverse(self,root,s):
        if root != None:   
            self.transverse(root.right,s)
            s.append(root.val)
            self.transverse(root.left,s)