#Iteration Solution1: use a queue to add each level of nodes into the queue, and check whether their vals are symmetric
#O(n) in time, O(n) in space
#AC in 59ms


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        row = [root]
        rowVal = [root.val]
        preRow = 1 #used to count how many elements in the row of last level
        curRow = 0 #used to count how many elements in current row when append nodes into the queue
        while len(row) > 0 :
            #iteration in every node from previous level
            for i in range(preRow):
                cur = row[0]
                row = row[1:]
                rowVal = rowVal[1:]
                
                if cur != None:
                    #add left node to the row and rowVal
                    row.append(cur.left)
                    if cur.left != None:
                        rowVal.append(cur.left.val)
                    else:
                        rowVal.append(None)
                    curRow += 1
                    #add right node to the row and rwoVal
                    row.append(cur.right)
                    if cur.right != None:
                        rowVal.append(cur.right.val)
                    else:
                        rowVal.append(None)
                    curRow += 1
                    
            #print(rowVal[0:int(len(row)/2)],rowVal[:int((len(row)-1)/2):-1])
                
            #Check whether left side of this level is equal to reverse order of right side of this level
            if rowVal[0:int(len(row)/2)] != rowVal[:int((len(row)-1)/2):-1]:
                return False
            
            #Assign current level node count to previous node count. Set current level node count to 0
            preRow = curRow
            curRow = 0
                    
        return True


###############################################################################
#Revursive solution2: compaire the outPair and inPair in the left branch and right branch of the tree
#O(n) in time, O(log(n)) in space
#

class Solution:
  	def isSymmetric(self, root):
	    if root is None:
	      	return True
	    else:
	      	return self.isMirror(root.left, root.right)

  	def isMirror(self, left, right):
	    if left is None and right is None:
	      	return True
	    if left is None or right is None:
	      	return False

	    if left.val == right.val:
	    	##################################################
	    	#Core of recursive way
	      	outPair = self.isMirror(left.left, right.right)
	      	inPiar = self.isMirror(left.right, right.left)
	      	##################################################
	      	return outPair and inPiar
	    else:
	      	return False






