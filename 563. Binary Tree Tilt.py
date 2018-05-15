#Solution1
#
#
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def node_sum(node):
            if not node:
                return 0
            l_sum, r_sum = node_sum(node.left), node_sum(node.right)
            self.tilt += abs(l_sum - r_sum)
            return l_sum + r_sum + node.val
        
        self.tilt = 0
        node_sum(root)
        return self.tilt


#Solution2
#
#AC in 1147ms
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Conner case
        if root == None:
            return 0

        #BFS to get all the tilt
        tilt = []
        queue = [root]
        while len(queue) != 0:
            cur = queue[0]
            queue = queue[1:]
            tilt.append(abs(self.transverse(cur.left,0) - self.transverse(cur.right,0)))
            if cur.left != None:
                queue.append(cur.left)
            if cur.right != None:
                queue.append(cur.right)   
        return sum(tilt)
        
        #tree transverse
    def transverse(self, root,total):
        if root == None:
            return 0
        else:
            total = root.val + self.transverse(root.left,total) + self.transverse(root.right,total)
        return total