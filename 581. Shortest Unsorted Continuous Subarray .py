#Idea: copy the nums and sort it, check which part is different
#O(nlog(n)) in time, O(n) in space
#AC in 83ms


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        newNums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i] != newNums[i]:
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j] != newNums[j]:
                break
        
        if j == 0 and i == len(nums)-1:
            return 0
        
        return j-i+1