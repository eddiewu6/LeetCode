#Idea, slipt by " ", remove "", return len
#O(n) in time, O(n) in space
#AC in 31ms

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or s == "":
            return 0
        slist = s.split(" ")
        count = 0
        for i in slist:
            if i != "":
                count += 1
        return count