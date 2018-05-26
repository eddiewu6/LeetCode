#
#O(n) in time,O(1) in space
#AC in 45ms

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 3:
            return False
        total = 1
        for i in range(2,int(num ** 0.5)+1):
            if num % i == 0:
                total = total + num / i + i
        if total == num:
            return True
        return False