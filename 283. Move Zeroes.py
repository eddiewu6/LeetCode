#Solution1 # find first 0 element, and find next non-zero element, swap
#O(n ** 2), O[1]
#AC in 288ms

class Solution1:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                for j in range(i+1,len(nums)):
                    if nums[j] != 0:
                        nums[i],nums[j] = nums[j],nums[i]
                        break
            i += 1


#Solution2 count how many 0 in the array, two pointers, i is the pointer of iteration to check elements in nums
#j is the pointer of non-zero element
#O(n) in time, O(1) in space
#AC in 60ms

class Solution2:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        countZero = nums.count(0)
        if countZero == 0:
            return
        i = 0
        j = 0
        while j < len(nums)-countZero and i < len(nums):
            # swap 0 element and non-zero element
            if nums[i] != 0 and i != j:
                nums[j] = nums[i]
                nums[i] = 0
                i += 1
                j += 1
            #continue the iteration for 0 element 
            elif nums[i] == 0:
                i += 1
            #Deal with i and j pointing at the same element situation
            elif nums[i] != 0 and i == j:
                i += 1
                j += 1