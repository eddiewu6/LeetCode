#Solution idea: use DFS with stack to find the maximum area of island
#O(n ** 3) in time, O(1) in space
#AC in 112ms


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0 #Represent the overall max Area
        tempMaxArea = 0 #Represent the temp max area for any island
        i = 0
        j = 0
        stack = []
        while i < len(grid):
            j = 0
            while j < len(grid[0]):
                if grid[i][j] == 1: #Found a new lead for an island
                    grid[i][j] = -1 #-1 means this point has been visited before
                    stack.append([i,j]) #Put the lead in the island
                    tempMaxArea = 1 #temp area count for this island is 1
                    while len(stack) != 0:# DFS loop with stack
                        cur = stack[-1]# current location
                        stack = stack[:len(stack)-1]#pop out current location from the stack
                        
                        if cur[0]-1 > -1:#check the location above
                            if grid[cur[0]-1][cur[1]] == 1:#check whether it is available
                                grid[cur[0]-1][cur[1]] = -1#if it is available, make it visted
                                tempMaxArea +=1#increas the temp area
                                stack.append([cur[0]-1,cur[1]])#push the location into stack
                        
                        if cur[0] + 1 < len(grid):#similar, check the location below
                            if grid[cur[0]+1][cur[1]] == 1:
                                grid[cur[0]+1][cur[1]] = -1
                                tempMaxArea +=1
                                stack.append([cur[0]+1,cur[1]])
                                              
                        if cur[1] - 1 > -1:#check the location at left side
                            if grid[cur[0]][cur[1]-1] == 1:
                                grid[cur[0]][cur[1]-1] = -1
                                tempMaxArea +=1
                                stack.append([cur[0],cur[1]-1])
                        
                        if cur[1] + 1 < len(grid[0]):#check the location at right side
                            if grid[cur[0]][cur[1]+1] == 1:
                                grid[cur[0]][cur[1]+1] = -1
                                tempMaxArea +=1
                                stack.append([cur[0],cur[1]+1])
                    maxArea = max(maxArea,tempMaxArea)#compair the area of this island with the area record
                j += 1
            i += 1
            
        return maxArea
