#Idea：Brutal Force to go over all the combinations of h and m.
#O(1) in time, O(n) in space
#AC in 40ms


class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for i in range(0,12):
            for j in range(0,60):
                if str(bin(i))[2:].count("1") + str(bin(j))[2:].count("1") == num:
                    res.append('%d:%02d' % (i, j))
        return res