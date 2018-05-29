#Use a mask of 3 element to check the flowerbed
#O(n) in time, O(1) in space
#AC in 115ms


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        countFlower = 0
        flowerbed.append(0)
        flowerbed = [0]+flowerbed
        i = 0
        while i < len(flowerbed) - 2:
            if flowerbed[i:i+3] == [0,0,0]:
                countFlower += 1
                #here why it is +2 is because of this case "1,0,0,0,0,0,1
                i += 2
            else:
                i += 1
        if countFlower < n:
            return False
        return True