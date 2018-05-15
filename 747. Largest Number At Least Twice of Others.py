#Idea is below
#O(n) in time, O(1) in space
#AC in 40ms

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or nums == []:
            return -1
        
        maximum = max(nums)#maximum number
        maxI = nums.index(maximum)#maximum number index
        
        nums = map(lambda x:x * 2,nums)#double all the elements in nums
        for i in nums:
            if i > maximum and i != maximum * 2:
                return -1
        return maxI