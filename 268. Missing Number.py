#Solution idea is to find the sum of 0 to n, find sum #of nums,sum of 0 to n minus sum of nums is the number 
#missing
#O(n) in time(Due to sum()), O(1) in space
#AC 43ms

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return 0
        k = len(nums)
        total = k*(k+1)/2
        total -= sum(nums)
        if total == 0:
            return 0
        return total