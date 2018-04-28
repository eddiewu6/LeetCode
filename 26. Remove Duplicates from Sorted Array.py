class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Corner case for empty list or None input
        if len(nums) == 0 or nums == None:
            return 0
        #Define the length of return,since the first element is always in the return, so initial value is 1
        count = 1
        #Iterator, there is always at least 1 element in the list
        i = 1 
        #Iterate for every elements in the nums
        while i < len(nums):
        # Check whehter current element is not the same as previous element, if yes, the element at position count is assigned         # to it. count plus one
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1  
            i += 1  
        return count