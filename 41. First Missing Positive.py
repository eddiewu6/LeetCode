###O(n) in time and O(1) in space
###Idea is to finde the min and max of the num in nums, and deal with different situation when min/max <0 or ==0 or >0
###AC
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Coner Case
        if len(nums) == 0:
            return 1
        #get max and min of the num in nums
        maxNum = max(nums)
        minNum = min(nums)
        #deal with [0,0,0,0],[1,1,1,1],[2,2,2,2],[-1,-1,-1,-1] and [0],[1],[2],[-1] kinds of situation
        if maxNum == minNum:
            if maxNum != 1:
                return 1
            else:
                return 2
        #if max less or equal to 0 and min is also less than 0 (not equal, which is dealed by previous if sentance), return 1
        if maxNum <= 0 and minNum < 0:
            return 1
        #if max larger than 0 and min larger or equal to 0, two situations:
        #1. min > 1, return 1
        #2. min = 0, find the smallest positive number which is not in the range(1,maxNum+2)
        if maxNum > 0 and minNum >= 0:
            if minNum > 1:
                return 1
            else:
                for i in xrange(1,maxNum+2):
                    if i not in nums:
                        return i
        #if max larger than 0 and min less than 0 (not equal, since equal has been dealed with in previous if sentance),
        #find the smallest positive number which is not in the range(1,maxNum+2)
        if maxNum > 0 and minNum < 0:
            for i in xrange(1,maxNum+2):
                if i not in nums:
                    return i
            return maxNum+1