#Solution idea: create string list, handle the string transform and combine them together.
#O(n) in time, O(n) in space
#AC  in 40ms

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        sss = S.split(" ")
        res = ""
        for i in range(len(sss)):
            if sss[i][0] in ["a","e","i","o","u","A","E","I","O","U"]:
                sss[i] = sss[i]+"ma"+"a"*(i+1)
            else:
                sss[i] = sss[i][1:]+sss[i][0]+"ma"+"a"*(i+1)
            res = res+" "+sss[i]
        return res[1:]