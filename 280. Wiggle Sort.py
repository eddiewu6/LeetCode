#Idea swap the adjacent element in the array and to make it wiggle sort
#O(n) in time, O(1) in space
#AC in 64ms beats 100%



class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) >= 2:
            i = 0
            while i < len(nums) - 1:
                if i % 2 == 0:
                    if nums[i] > nums[i+1]:
                        nums[i],nums[i+1] = nums[i+1],nums[i]
                else:
                    if nums[i] < nums[i+1]:
                        nums[i],nums[i+1] = nums[i+1],nums[i]
                i += 1
        