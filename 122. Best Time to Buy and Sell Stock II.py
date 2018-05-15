#Idea, gready
#O(n) in time, and O(1) in space
#AC in 48ms

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        res = 0
        i = 0
        
        while i < len(prices)-1:
            cur = prices[i]# use to record current bottom value
            tempmax = prices[i]# use to record current temp max value
            for j in range(i+1,len(prices)):
                #looking for peak value after i
                if prices[j] > tempmax:
                    tempmax = prices[j]
                #if the peak value is found or the j reach the end, sum the profit
                if prices[j] < tempmax or j == len(prices)-1:
                    res += tempmax-cur
                    break
            i = j#move bottom pointer to j
        return res