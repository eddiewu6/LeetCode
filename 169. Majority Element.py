#Idea: create hashtable to find the count of each individual element in the nums, check which one is larger than len(nums)/2

#O(n) in time, O(n) in space
#AC in 52ms

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = dict().fromkeys(nums,0)
        for i in temp.keys():
            temp[i] = nums.count(i)
            if temp[i] >= len(nums)/2:
                return i