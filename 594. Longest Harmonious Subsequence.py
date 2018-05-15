#Solution1 use hashtable with keys of the num in nums, values are their count. Find max(res, dic[k] + dic[k + 1])
#O(n) in time, O(n) in space
#AC

class Solution(object):
    def findLHS(self, nums):
        dic, res = collections.defaultdict(int), 0
        for num in nums: dic[num] += 1
        for k in dic:
            if k + 1 in dic: res = max(res, dic[k] + dic[k + 1])
        return res


#Solution2, sort the array, and find max of target's count + (target+1)'s count
#O(nlogn) in time, O(1) in space
#AC in 356ms


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == [] or nums == None:
            return 0
        #Deal with [1,1,1,1] situation
        if max(nums) == min(nums):
            return 0
        nums.sort()
        maxlen = 0
        i = 0
        while i + maxlen < len(nums):
            countTar = 1#count of target
            countTarNext = 0#count of target+1
            target = nums[i]
            
            j = i + 1
            while j < len(nums):
                if nums[j] == target:
                    countTar += 1
                if nums[j] == target + 1:
                    countTarNext += 1
                if nums[j] > target + 1: # jump out of the loop
                    j = len(nums)
                else:
                    j += 1
            
            count = countTar + countTarNext #length
                        
            if count > maxlen and countTarNext != 0: # deal with [1,3,5,7,9] situation
                maxlen = count
            i += countTar #iteration to next target, which is target+1
        
        return maxlen