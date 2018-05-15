#Solution1 DFS with recursive
#O(??????) in time, O(n) in space
#

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        return self.dfs(root, k, [])

    def dfs(self, root, k, d):
        if root is None:
            return False
        if root.val in d:
            return True
        else:
            d.append(k - root.val)
            print(d)
        return self.dfs(root.left, k, d) or self.dfs(root.right, k, d)



#Solution2 DFS with stack and iteration
#
#AC in 764ms
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        stack = [root]
        res = []
        while len(stack) != 0:
            cur = stack[-1]
            stack = stack[:len(stack)-1]
            #res = res[:len(res)-1]
            if cur.val in res:
                return True
            else:
                res.append(k-cur.val)
                if cur.left != None:
                    stack.append(cur.left) 
                if cur.right != None:
                    stack.append(cur.right)           
        return False
