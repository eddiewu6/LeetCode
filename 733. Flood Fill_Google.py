#Use DFS to find all connected image[sr][sc] and make them -1, color all the -1 to newColor
#O(m*n) in time, O(m*n) in space
#AC in 76ms
class Solution:
    def floodFill(self, image, sr, sc):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # Boundary check
        if image == None:
            return None
        if sr >= len(image) or sr < 0:
            return image
        if sc >= len(image[0]) or sr < 0:
            return image

        #Get opposite color
        if image[sr][sc] == 0:
            self.newColor = 1
        else:
            self.newColor = 0
        
        #DFS and mark all accessable grid as -1
        self.searchAll(image,sr,sc)

        return image
        
        
    #DFS with stack
    def searchAll(self,image, sr, sc):

        stack = [[sr,sc]]
        curColor = image[sr][sc]
        image[sr][sc] = self.newColor

        while len(stack) != 0:
            #curPos is the iterator
            curPos = stack[-1]
            stack = stack[:len(stack)-1]


            #Check 4 directions of current position
            if curPos[0] > 0:
                if image[curPos[0]-1][curPos[1]] == curColor:
                    image[curPos[0]-1][curPos[1]] = self.newColor
                    stack.append([curPos[0]-1,curPos[1]])
            if curPos[0] < len(image)-1:
                if image[curPos[0]+1][curPos[1]] == curColor:
                    image[curPos[0]+1][curPos[1]] = self.newColor
                    stack.append([curPos[0]+1,curPos[1]])
            if curPos[1] > 0:
                if image[curPos[0]][curPos[1]-1] == curColor:
                    image[curPos[0]][curPos[1]-1] = self.newColor
                    stack.append([curPos[0],curPos[1]-1])
            if curPos[1] < len(image[0])-1:
                if image[curPos[0]][curPos[1]+1] == curColor:
                    image[curPos[0]][curPos[1]+1] = self.newColor
                    stack.append([curPos[0],curPos[1]+1])
        return