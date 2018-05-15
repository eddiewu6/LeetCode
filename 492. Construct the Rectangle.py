#Solution idea: start from sqrt of area, find i * j == area
#O(n) in time, O(1) in space
#AC in 1556ms

class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area <= 0:
            return []
        
        posL = int(area ** 0.5)
        for i in range(posL,area+1):
            if area % i == 0:
                return [max(i,int(area / i)),min(i,int(area / i))]