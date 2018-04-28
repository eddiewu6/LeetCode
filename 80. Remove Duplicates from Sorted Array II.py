class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for n in nums:
            if count < 2 or n > nums[count-2]:
                nums[count] = n
                count += 1
        return count
    
    def removeDeplicates2(self,nums):
        
        if not nums:
            return 0
        count = 0 
        for i in range(1,len(nums)):
            if nums[count] != nums[i] or (count>0 and nums[count] != nums[count-1]) or count==0:
                count += 1
                nums[count] = nums[i]
        return count+1