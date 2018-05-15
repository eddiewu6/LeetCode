#Idea: sort the nums and find the ranks; modify the original list as required
#O(n) in time, O(n) in space
#AC in 122ms


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        table = dict().fromkeys(nums)
        orig = nums[:]
        orig.sort(reverse = True)
        for i in range(len(orig)):
            table[orig[i]] = i
        for i in range(len(nums)):
            if table[nums[i]] == 0:
                nums[i] = "Gold Medal"
            elif table[nums[i]] == 1:
                nums[i] = "Silver Medal"
            elif table[nums[i]] == 2:
                nums[i] = "Bronze Medal"
            else:
                nums[i] = str(table[nums[i]]+1)
        return nums