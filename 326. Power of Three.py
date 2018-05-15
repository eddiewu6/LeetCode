#Idea: find the maximum integer of power of 3, and check the residule of that number % n
#O(1) in time, O(1) in space
#AC in 250ms


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return  n > 0 and 1162261467 % n == 0 #1162261367 is the maximum numbder of power of 3 within the range of 32bit integer.