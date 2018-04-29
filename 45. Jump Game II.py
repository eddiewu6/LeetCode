#Solution 1 which has timing issue with recursive DP, only 62/90 cases passed

class Solution:    
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nodeConnection = []#nodeConnection[i] means all the node before i have direct access to node i
        for i in range(len(nums)-1,-1,-1):
            row = []
            for j in range(i-1,-1,-1):
                if nums[j] >= i - j:
                    row.append(j)
            #row = row.reverse()
            nodeConnection.append(row)
        nodeConnection.reverse()
        #print(nodeConnection)
        
        minSteps = [0]*len(nums)
        i = 1
        while i < len(nums):
            minSteps[i] = self.minStepToZero(i,nodeConnection)
            i += 1
        
        
        
        return minSteps[-1]
                
    """
    Use DP to get the minimum step count to the index 0 at index node
    """
    def minStepToZero(self,node,maptable):#node stands for the index
        
        
        #Recursive has to calculate privious steps at node i again, which will cause time exceed limitation issue
        
        if 0 in maptable[node] or maptable[node] == []:
            return 1
        else:
            temp = []
            for i in maptable[node]:
                temp.append(self.minStepToZero(i,maptable))
            return min(temp) + 1


###################################################################
#Sulotion 2 use iteration to resolve the timing issue, but only 90/92 cases passed
#DP is not good idea in this problem

class Solution2:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Corner case
        if len(nums) == 1:
            return 0
        
        #Generate a map
        nodeConnection = []#nodeConnection[i] means all the node before i have direct access to node i
        for i in range(len(nums)-1,-1,-1):
            row = []
            for j in range(i-1,-1,-1):
                if nums[j] >= i - j:
                    row.append(j)
            nodeConnection.append(row)
        nodeConnection.reverse()
        
        
        
        #minSteps is used to store the min step count from index i to 0, DP is used.
        minSteps = [0]*len(nums)
        minSteps[0],minSteps[1] = 0,1
        for i in range(2,len(nums)):
            if 0 in nodeConnection[i]:
                minSteps[i] = 1
            else:
                minSteps[i] = min(minSteps[j] for j in nodeConnection[i]) + 1
                
        
        return minSteps[-1]


###################################################################
#Sulotion3
#Use greedy to find the maxstep for each i 

class Solution3:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Corner case
        if len(nums) == 1:
            return 0
        
        
        last_max_reach, current_max_reach = 0 , 0
        njump , i = 0 , 0
        while current_max_reach < len(nums)-1:
            while i <= last_max_reach:
                current_max_reach = max(i+nums[i],current_max_reach)
                i+=1
            """
            ###This is used to deal with invalid input
            if last_max_reach == current_max_reach:
                return -1
            """
            last_max_reach = current_max_reach
            njump += 1
        return njump
        