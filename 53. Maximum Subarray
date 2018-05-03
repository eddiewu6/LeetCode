#Solution 1 DP
#O(n) in time, O(1) in space
#AC in 48ms


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        current_max = 0
        result = nums[0]
        for n in nums:
            current_max += n
            result = max(current_max,result)
            current_max = max(0, current_max)
        return result


#Solution 2 Divide and Conquer
#O(nlogn) in time, O(1) in space
#AC in 120ms
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left_max = self.maxSubArray(nums[:int(len(nums)/2)])
        right_max = self.maxSubArray(nums[int(len(nums)/2):])
        
        right_tmp = nums[int(len(nums)/2)]
        left_tmp = nums[int(len(nums)/2)-1]
        
        sums = 0
        for num in reversed(nums[:int(len(nums)/2)]):
            sums = sums + num
            if sums > left_tmp:
                left_tmp = sums
       
                
        sums = 0
        for num in nums[int(len(nums)/2):]:
            sums = sums + num
            if sums > right_tmp:
                right_tmp = sums
        
        return max(left_max, right_max, right_tmp+left_tmp)