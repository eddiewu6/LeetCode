#Idea, find all nodes in s with same value as t.val, check the subtree is identical to t
#O(n) in time, O(n) in space
#AC in 568ms


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.startNode = []
        self.findNode(s,t.val)
        #if there is no nodes with same val as t.val, return False
        if len(self.startNode) == 0:
            return False
        #else for each of them, check whehter they have the same tree structure as t
        else:
            for i in self.startNode:
                if self.compareTree(i,t):
                    return True
        return False
            
    #Compare tree s and tree t, to see whehter thay are identical
    def compareTree(self,s,t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        
        if s.val == t.val:
            return self.compareTree(s.left,t.left) and self.compareTree(s.right,t.right)
        else:
            return False
        return True
    
    #Find all nodes has same val as val in tree root, return a list of all the nodes has the same val 
    def findNode(self,root,val):
        if root == None:
            return None
        if root.val == val:
            self.startNode.append(root)
            
        self.findNode(root.left,val)
        self.findNode(root.right,val)


#Solution2, use isEqual to check whether s1 and s2 are identical;
#Use a queue to store all the nodes in tree s; Iteration through the queue and check whether the subtree in queue is identical to t
#O(m+n) in time, O(n) in space
#AC



def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isEqual(s1,s2):
            if s1 == None or s2 == None:
                return s1==s2
            if s1.val != s2.val:
                return False
            return isEqual(s1.left,s2.left) and isEqual(s1.right,s2.right)
        
        queue = []
        queue.append(s)
        while queue:
            node = queue.pop(0)
            if isEqual(node, t):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

