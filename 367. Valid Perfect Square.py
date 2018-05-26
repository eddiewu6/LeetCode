#Binary search for the answer
#O(log(n)) in time, O(1) in space
#AC in 49ms



class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        
        left = 1
        right = num
        #Make sure left != right -1, since it will go into infinite loop if so
        while left < right - 1:
            mid = (left + right) / 2
            #print(mid,left,right)
            if mid * mid > num:
                right = mid
            elif mid * mid < num:
                left = mid
            else:
                return True
        return False