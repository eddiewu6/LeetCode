#Use a list store all the val, and sort them, find the minimum abs distance
#
#AC in 72ms


class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = []
        self.transverse(root,s)
        s.sort()
        res = sys.maxsize
        for i in range(1,len(s)):
            if abs(s[i]-s[i-1]) < res:
                res = abs(s[i]-s[i-1])
        return res
    
    def transverse(self,root,s):
        if root != None:
            self.transverse(root.left,s)
            s.append(root.val)
            self.transverse(root.right,s)