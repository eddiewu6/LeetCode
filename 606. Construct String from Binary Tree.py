#Solution idea: 
#O(?) in time,O(?) in space
#AC in 68ms


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        res = str(t.val)
        if not t.left and t.right:
            res = res + "()(" + self.tree2str(t.right) + ")"
        else:
            if t.left:
                res = res + "("+self.tree2str(t.left)+")"
            if t.right:
                res = res + "("+self.tree2str(t.right)+")"
        return res