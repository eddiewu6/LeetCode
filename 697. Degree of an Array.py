#Idea is below
#O(n ** 2) in time, O(n) in space
#AC in 756ms

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Coner case
        if nums == []:
            return 0
        if  len(nums) == 1:
            return 1
        #Count the frequency of each number
        table = dict().fromkeys(nums,0)
        for i in range(len(nums)):
            table[nums[i]] += 1
        #target list is used to store all the maximum frequency number
        target = []
        maxcount = 0
        #find all maximum frequencies
        for i in table.items():
            if i[1] > maxcount:
                maxcount = i[1]
        #find all maximum frequencies number
        for i in table.items():
            if i[1] == maxcount:
                target.append(i[0])
        
        #Find minimum distance for each maximum frequence number 
        minDis = 50001
        for i in target:
            start = nums.index(i)
            end = len(nums) - nums[::-1].index(i) - 1
            if minDis > (end - start):
                minDis = end - start
        return minDis+1
            