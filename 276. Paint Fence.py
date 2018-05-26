#Solution idea DP: The nth result depends on whether previous 2 has the same color or not
#if they have same color, the nth post color can have k-1 cases,so it is same*(k-1)
#if they have different color, you can either paint same color as previous one dif*1 or different as previous one dif*(k-1)
#O(n) in time, O(1) in space
#AC in 30ms


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same = k
        dif = k * (k - 1)
        for i in range(3, n+1):
            same, dif = dif, (same+dif)*(k-1)
        return same + dif