#Idea: remove all factors that is 2,3,5, check what is left behind
#O(log(n)) in time, O(1) in space
#AC

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num == 0:
            return False
        if num < 0:
            return False
        
        while num % 2 == 0:
            num = num / 2
        while num % 3 == 0:
            num = num / 3
        while num % 5 == 0:
            num = num / 5
        if num == 1:
            return True
        return False