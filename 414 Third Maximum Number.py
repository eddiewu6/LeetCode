class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = -2147483649;
        max2 = -2147483649;
        max3 = -2147483649;
        
        for i in nums:
            if (i>max1):
                if max2 <> -2147483649:
                    max3 = max2
                if max1 <> -2147483649:
                    max2 = max1
                max1 = i                
            if (i>max2) and (i<max1):
                if max2 <> -2147483649:
                    max3 = max2
                max2 = i
            if ((i>max3) and (i<max2)):
                max3 = i
        if max3 <> -2147483649:
            return max3
        else:
            return max1
            