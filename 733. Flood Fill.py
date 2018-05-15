#Use DFS to find all connected image[sr][sc] and make them -1, color all the -1 to newColor
#O(m*n) in time, O(m*n) in space
#AC in 76ms
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        if image == None:
            return None
        if sr >= len(image) or sr < 0:
            return image
        if sc >= len(image[0]) or sr < 0:
            return image
        self.searchAll(image,sr,sc)
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == -1:
                    image[i][j] = newColor
        return image
        
        
        
    def searchAll(self,image, sr, sc):
        stack = [[sr,sc]]
        curColor = image[sr][sc]
        #print(curColor)
        image[sr][sc] = -1
        while len(stack) != 0:
            #print(stack)
            curPos = stack[-1]
            stack = stack[:len(stack)-1]
            if curPos[0] > 0:
                if image[curPos[0]-1][curPos[1]] == curColor:
                    image[curPos[0]-1][curPos[1]] = -1
                    stack.append([curPos[0]-1,curPos[1]])
            if curPos[0] < len(image)-1:
                if image[curPos[0]+1][curPos[1]] == curColor:
                    image[curPos[0]+1][curPos[1]] = -1
                    stack.append([curPos[0]+1,curPos[1]])
            if curPos[1] > 0:
                if image[curPos[0]][curPos[1]-1] == curColor:
                    image[curPos[0]][curPos[1]-1] = -1
                    stack.append([curPos[0],curPos[1]-1])
            if curPos[1] < len(image[0])-1:
                if image[curPos[0]][curPos[1]+1] == curColor:
                    image[curPos[0]][curPos[1]+1] = -1
                    stack.append([curPos[0],curPos[1]+1])
        return