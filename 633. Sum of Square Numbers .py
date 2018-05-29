#Idea: check the number 0 : c**0.5 + 1,check whether the rest can be a integer
#O(n) in time, O(1) in space
#AC

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        b = int(c ** 0.5) + 1
        
        for i in range(b):
            a = (c - i ** 2) ** 0.5
            if a % 1 == 0.0:
                return True
        return False