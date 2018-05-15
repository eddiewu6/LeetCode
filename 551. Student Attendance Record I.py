#Solution
#O(n) in time, O(1) in space
#AC in 36ms
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None:
            return False
        if s.count("A") > 1 or s.count("LLL") > 0:
            return False
        return True
