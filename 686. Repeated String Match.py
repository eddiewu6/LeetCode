#
#
#
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        lenA = len(A)
        lenB = len(B)
        reps = lenB / lenA
        if B in A: return 1
        elif B in A*reps: return reps
        elif B in A*reps + A: return reps+1
        elif B in A*reps + A + A: return reps+2
        
        return -1