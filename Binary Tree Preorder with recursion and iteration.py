# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Preorder with recursive
class Solution(object):
    def preorderTraversal(self, root):
        
        #:type root: TreeNode
        #:rtype: List[int]
        
        self.res = []
        self.traverse(root)
        return self.res
        
    def traverse(self, root):
        
        if root == None:
            return None
        else:
            self.res.append(root.val)
            self.traverse(root.left)
            self.traverse(root.right)

#Preoder with iteration and stack
class Solution(object):
    def preorderTraversal(self, root):
        if root == None:
            return []
        stack = [root]
        res = []
        while len(stack) >0:
            cur = stack.pop()
            
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            
        return res