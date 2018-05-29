#Idea:
#O(m*n) in time, O(n) in space
#AC in 35ms


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) < 3:
            return 0
        if len(grid[0]) < 3:
            return 0
        #table used to record the possible top left corner of the magic square
        table = []
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if sum(grid[i][j:j+3]) == 15 and grid[i][j]+grid[i+1][j]+grid[i+2][j] == 15:
                    table.append((i,j))
        #Count how many magic square is there.
        res = 0
        for pos in table:
            if self.checkSquare(grid,pos[0],pos[1]):
                res += 1
        return res
        
    def checkSquare(self,grid,i,j):
        #the magic square cannot contain 10
        for m in range(i,i+3):
            for n in range(j,j+3):
                if grid[m][n] == 10:
                    return False
        #check the sum of each row and colomn
        return sum(grid[i+1][j:j+3]) == 15 and sum(grid[i+2][j:j+3]) == 15 and grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1] == 15 and grid[i][j+2]+grid[i+1][j+2]+grid[i+2][j+2] == 15 and grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2] == 15 and grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j] == 15
        
        
    