#solution1: use slice

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if j < 0:
            return 0
        if i <= j:
            if i <= 0:
                return sum(self.nums[:j+1])
            else:
                return sum(self.nums[i:j+1])



#solution2
#
#AC in 70ms

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        #used to store the sum(nums[0:i+1])
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i]



