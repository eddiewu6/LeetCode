# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Level order traversal with Queue(Breadth first)
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root == None:
            return []
        queue = [root]
        res = []
        while len(queue) > 0:
            row = []
            for i in range(len(queue)):
                cur = queue[0]
                queue = queue[1:]
                row.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(row)
        return res