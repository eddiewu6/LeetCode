#Idea, do not use sum(nums[i:i+k]) since this cause high time consumption. Reduce the head element and add a tail element to previous total sum
#O(n) in time, O(1) in space
#AC in 165ms


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if nums == [] or nums == None:
            return 0
        
        maximum = -300000001
        total = sum(nums[0:k])
        for i in range(len(nums) - k):
            if total  > maximum:
                maximum = total
            total = total - nums[i] + nums[i+k]
        #Max is used to dial with [5],1 situation
        return max(float(maximum),float(total)) / k