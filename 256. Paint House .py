#Use DP to find all possibilities
#O(n) in time, O(n) in space
#AC in 44ms

class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0    
        dp = costs[0]
        for i in range(1, len(costs)):
            dp = [min(costs[i][0] + dp[1], costs[i][0] + dp[2]), 
                  min(costs[i][1] + dp[0], costs[i][1] + dp[2]), 
                  min(costs[i][2] + dp[0], costs[i][2] + dp[1])]
        return min(dp)