#idea: sort the array first, use Brutal force to finde each pair and add them into a set to remove duplicates
# O(n ** 2) in time, O(n) in space
# 60/72 cases passed, time limit exceeded

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashset = set()
        nums.sort()
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    hashset.add((nums[i],nums[j]))
        return len(hashset)



#Solution2
#
#61/72 cases passed, time limit exceed
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        #nums.sort()
        if k < 0:
            return 0
        if k > 0:
            hashset = set()
            for i in range(len(nums)):
                if nums[i]-k in nums:
                    temp = [nums[i],nums[i]-k]
                    temp.sort()
                    hashset.add(tuple(temp))
                if nums[i]+k in nums:
                    temp = [nums[i],nums[i]+k]
                    temp.sort()
                    hashset.add(tuple(temp))
            return len(hashset)
        if k == 0:
            count = 0
            hashset = set(nums)
            for i in hashset:
                if nums.count(i) > 1:
                    count += 1
            return count