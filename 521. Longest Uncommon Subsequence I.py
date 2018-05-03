#Solution idea: check corner case for empty string, return larger length if their length are different
#If length is same, check whether they are identical, it identical, return -1
#if not, return length of either one
#O(1), O(1)
#AC in 32ms

class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) == 0 and len(b) != 0:
            return len(b)
        if len(b) == 0 and len(a) != 0:
            return len(a)
        if len(a) == 0 and len(b) == 0:
            return -1
        if len(a) > len(b):
            return len(a)
        if len(a) < len(b):
            return len(b)
        if len(a) == len(b):
            if a == b:
                return -1
            else:
                return len(a)