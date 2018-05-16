#Idea: sort the nums, find the same nums[i] and nums[i+1]; use set to find the missing elements
#O(nlogn) in time, O(n) in space
#AC in 186ms


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        correctSet = set(range(1,len(nums)+1))
        res = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                res.append(nums[i])
                break
                
        nums = set(nums)
        res.append((correctSet - nums).pop())
        return res


#Solution 2 idea:
#
#
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sall = sum(list(range(1, len(nums)+1)))
        sset = sum(set(nums))
        snum = sum(nums)

        miss    = sall - sset
        repeat  = snum - sset

        return [repeat, miss]