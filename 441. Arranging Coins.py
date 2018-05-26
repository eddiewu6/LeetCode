#Idea: find the number num where num*(num+1)/2 <= n and (num+1)*(num+1+1)/2 > n
#O(1) in time, O(1) in space
#AC in 56ms

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        start = int((2 * n) ** 0.5)
        while start * (start + 1) <= 2 * n:
            start += 1
        return start - 1