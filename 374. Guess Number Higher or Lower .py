#Idea: binary search
#O(log(n)) in time, O(1) in space
#AC in 31ms

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1
        upper = n + 1 # plus one is necessary for binary search with base 1
        mid = (lower + upper) // 2
        guesss = guess(mid)
        while guesss != 0:
            guesss = guess(mid)
            if guesss == -1:
                upper = mid
            elif guesss == 1:
                lower = mid
            mid = int((lower + upper) / 2)
        return mid