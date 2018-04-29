class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False 
        maxnum = 0
        for i in range(len(nums)):
            if i > maxnum: # Deal with [4,3,2,1,1,0,4] situation
                return False
            elif maxnum == len(nums)-1: # the longest step can reach the final point
                return True
            else:
                maxnum = max(nums[i]+i,maxnum) # find the longest distance frome start point that it can reach
        return maxnum > len(nums)-1