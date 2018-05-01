#Solution 1， sort the array, and all the even index is the 
#O(nlogn) in time, O(1) in space
#AC in 120ms
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        return sum(nums[::2])