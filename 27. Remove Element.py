class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #Deal with corner case
        if nums == None or len(nums) == 0:
            return 0
        #Count how many elements are not val
        count = 0
        #Iterator
        i = 0
        """
        Check every element, to see whether it is val. If it is not val, count++. If it is val, find next not val element, and swap the value
        
        """
        while i < len(nums)-count:
            if nums[i] != val:
                count += 1
            else:
                j = i + 1
                while j < len(nums):
                    if nums[j] != val:
                        nums[i],nums[j] = nums[j],nums[i]
                        count += 1
                        break
                    j += 1
            i += 1
        return count
        