#Idea: Find the depth of subtrees and check their difference, whether it is larger than 1 or not
#O(n ** 2) in time, O(n) in space
#AC in 137ms



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        #Use BFS to transverse the tree
        queue = [root]
        while len(queue) > 0:
            cur = queue[0]
            queue = queue[1:]
            #Check the height of each tree
            if abs(self.findHeight(cur.left) - self.findHeight(cur.right)) > 1:
                return False
            
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
                
        return True
        
        
    def findHeight(self, root):
        if root ==  None:
            #Used to balance the +1
            return -1
        else:   
            return max(self.findHeight(root.left),self.findHeight(root.right)) + 1