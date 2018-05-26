#Solution 1 idea: DFS with stack to go over the tree nodes, and calculate the count for each element
#O(n ** 2) in time, O(n) in space
#AC in 183ms

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        #DFS
        stack = [root]
        maxCount = -1
        maxVal = []#Store value with maxCount
        while len(stack) != 0:
            cur = stack[0]
            stack = stack[1:]

            curCount = self.countSameNode(cur,cur.val)
            if curCount > maxCount:
                maxCount = curCount
                maxVal=[cur.val]
            elif curCount == maxCount:
                maxVal.append(cur.val)
                
            #Append the left and right children of cur node
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
                
        return maxVal
    
    #used to count the same value as data nodes in the tree
    def countSameNode(self, root, data):
        if root == None:
            return 0
        else:
            if root.val < data:
                return self.countSameNode(root.right, data)
            if root.val > data:
                return self.countSameNode(root.left, data)
            if root.val == data:
                return 1 + self.countSameNode(root.left, data) + self.countSameNode(root.right, data)


   #Idea 2: dfs with recursive
   #O(n) in time, O(1) in space
    
   class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        self.curVal = root.val - 1
        self.curNum = 0
        self.maxNum = 0
        self.maxVals = []
        
        def dfs(root):
            if root is not None:
            
                dfs(root.right)
            
                if root.val != self.curVal:
                    self.curNum = 0
                self.curNum = self.curNum + 1
                self.curVal = root.val
                if self.curNum == self.maxNum:
                    self.maxVals.append(self.curVal)
                elif self.curNum > self.maxNum:
                    self.maxNum = self.curNum
                    self.maxVals = []
                    self.maxVals.append(self.curVal)
                
                dfs(root.left)
        
        dfs(root)
        return self.maxVals
