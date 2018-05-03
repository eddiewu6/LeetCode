#Solution 1 use count list to count the previous to current 1's number,finde max #of them
#O(n) in time, O(n) in space
#AC in 164ms
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or nums == None:
            return 0
        count = [0]*len(nums)
        count[0] = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == 1:
                count[i] = count[i-1]+1
        return max(count)


#Solution 2 idea: use tempcount to calculate current number of consective 1s, compair
# with maxcount, which is the maximum count of consective 1s of the whole list.
#Remember to deal with [1,1,1,1,1] situation
#O(n) in time, and O(n) in space
#AC in 104ms
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or nums == None:
            return 0
        maxcount = 0
        tempcount = 0
        for i in range(len(nums)):
            
            if nums[i] == 1:
                tempcount += 1
                #deal with [1,1,1,1,1,1] situation
                if i == len(nums)-1:
                    return max(maxcount,tempcount)
            if nums[i] == 0:
                maxcount = max(maxcount,tempcount)
                tempcount = 0
        return maxcount