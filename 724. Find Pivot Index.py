#Solution1
#O(n ** 2) in time, O(1) in space
#733/741 cases passed, time limit exceeded

class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return -1
        if len(nums) == 0:
            return -1
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

#Solution2, optimize the sum function by leftsum and rightsum
#O(n) in time, O(1) in space
#AC in 72ms

class Solution2:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return -1
        if len(nums) == 0:
            return -1
    
        leftsum = 0
        rightsum = sum(nums)-nums[0]
        if leftsum == rightsum:
            return 0
        
        for mid in range(1,len(nums)):
            leftsum += nums[mid-1]
            rightsum -= nums[mid]
            if leftsum == rightsum:
                return mid
        return -1
