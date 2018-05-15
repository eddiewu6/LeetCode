#Solution idea : find next start, check whether next start is the last element in the bits
# O(n) in time, O(1) in space
#AC in 40ms
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        nextStart = 0
        while nextStart < len(bits):
            if bits[nextStart] == 1:
                nextStart += 2
            elif bits[nextStart] == 0:
                nextStart += 1
            if nextStart == len(bits)-1:
                return True
        return False