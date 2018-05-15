#Solution1 idea: sort list, and find the max between max1*max2*max3 and max1*min1*min2
#O(nlogn) in time, O(1) in space
#AC in 104ms


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])


#Solution2 idea: find the max between max1*max2*max3 and max1*min1*min2
#O(n) in time, O(1) in space
#AC in 88ms


 class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = -1001
        min1 = min2 = 1001
        for i in range(len(nums)):
            if nums[i] > max1:
                max3 = max2
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2:
                max3 = max2
                max2 = nums[i]
            elif nums[i] > max3:
                max3 = nums[i]

            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]
        #print(max1,max2,max3,min1,min2)
        return max(max1*max2*max3,max1*min1*min2)