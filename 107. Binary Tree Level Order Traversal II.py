#Solution idea
#O(n) in time, O(n) in space
#AC in 44ms


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = [[root.val]]
        lastlevelcount = 1 #used to count elements in previous level, here it is level 1, root level
        while len(queue) != 0:
            thislevelcount = 0#used to count the elements in current level
            for i in range(0,lastlevelcount):#leftpop all previous level elements, and add their leaf elements into the queue, count how many leaves there are.
                cur = queue[0]
                queue = queue[1:]
                
                if cur.left != None:
                    thislevelcount += 1
                    queue.append(cur.left)
                if cur.right != None:
                    thislevelcount += 1
                    queue.append(cur.right)
            lastlevelcount = thislevelcount #assign last level as previous level
            
            #put all of this levels elements into the row and append them to the res
            row = []
            for i in queue:
                row.append(i.val)
            #remove the empty row
            if row != []:
               res.append(row)
        #reverse the results
        res = res[::-1]
        return res
            
        
        