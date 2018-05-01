#Solution idea: find the minimum steps to each grid with DP(minSteps[i][j] = min(minSteps[i-1][j],minSteps[i][j-1]) + grid[i]
#[j]).
#O(n ** 2) in time, O(n ** 2) in space
#AC in 64ms

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Creat a matrix to store the minimum step count to node i,j
        minSteps = []
        for i in range(len(grid)):
            row = [0]*len(grid[0])
            minSteps.append(row)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0:#Deal with the top row to prevent list index out of boundary
                    minSteps[i][j] = sum(grid[i][:j+1])
                elif j == 0:#Deal with the left column to prevent list index out of boundary
                    minSteps[i][j] = sum(grid[i][j] for i in range(i+1))
                else:#Deal with the rest grid
                    minSteps[i][j] = min(minSteps[i-1][j],minSteps[i][j-1]) + grid[i][j]
        return minSteps[-1][-1]