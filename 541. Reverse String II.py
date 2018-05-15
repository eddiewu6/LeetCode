#Idea: divide the by list into len(list)/k blocks, reverse the even blocks on 0 bases
#O(n**2) in time, O(1) in space
#AC in 64ms


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if s == None:
            return None
        if k >= len(s):
            return s[::-1]
        ss = list(s)
        res = ""
        i = 0
        while i*k < len(s):
            if i % 2 == 0:
                if i == 0:
                    res += "".join(ss[(i+1)*k-1::-1])
                else:
                    res += "".join(ss[(i+1)*k-1:i*k-1:-1])
                #print(res)
            else:
                res += "".join(ss[i*k:(i+1)*k])
            i+=1
        res += "".join(ss[i*k:])
        return res
        