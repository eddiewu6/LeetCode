#Solution idea: creat a full set of 1 to n, transform the nums into set to remove
#duplicates. Do set subtraction, and transform the set into list
#O(n) in time,O(n) in space
#AC in 156ms


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set([i for i in range(1,len(nums)+1)])
        nums = set(nums)
        res = list(res - nums)
        return res