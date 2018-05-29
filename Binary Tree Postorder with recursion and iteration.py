# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Postorder traversal with recursion
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.traversal(root)
        return self.res
        
    def traversal(self,root):
        if root == None:
            return None
        self.traversal(root.left)
        self.traversal(root.right)
        self.res.append(root.val)
        

#Postorder traversal with iteration, stack and set
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        res = []
        stack = []
        visited = set()
        cur = root
        
        while len(stack) > 0 or cur!=None:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if cur.right != None and not cur.right in visited:
                    stack.append(cur)
                    cur = cur.right
                else:
                    visited.add(cur)
                    res.append(cur.val)
                    cur = None
        return res
            
        