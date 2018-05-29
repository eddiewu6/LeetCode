# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Inorder traverse with recursion
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.traverse(root)
        return self.res
        
    def traverse(self,root):
        if root  == None:
            return None
        else:
            self.traverse(root.left)
            self.res.append(root.val)
            self.traverse(root.right)


#Inorder traverse with iteration
class Solution(object):
    def inorderTraversal(self, root):
        if root == None:
            return []
        
        stack = []
        res = []
        cur = root
        while len(stack) > 0 or cur != None:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            
        return res