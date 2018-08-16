#Hashmap
#O(m+n) in time, O(m+n) in space
#AC in 24ms
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        AB = (A + " "+ B).split(" ")
        ABmap = {}
        ABmap = ABmap.fromkeys(AB,0)
        for i in AB:
            ABmap[i] += 1
        res = []
        for i in ABmap:
            if ABmap[i] == 1:
                res.append(i)
        return res
        