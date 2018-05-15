#idea
#O(n) in time, O(1) in space
#AC in 36ms
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        current = max_length = 1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                current += 1
                max_length = max(max_length,current)
            else:
                current = 1
        return max_length