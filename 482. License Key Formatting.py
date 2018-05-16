#
#O(n) in time, O(n) in space
#Exceed time limit after 34 cases

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper()
        S = S.replace("-","")
        res = S[:(len(S) % K)] + "-"
        i = 0
        while i < (len(S) / K):
            res = res + S[(len(S) % K) + i * K : (len(S) % K) + (i + 1) * K] + "-"
            i += 1
        
        if len(S) % K == 0:
            return res[1:len(res)-1]
        else:
            return res[:len(res)-1]

#Solution2

#AC in 39ms


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '')[::-1].upper()
        return '-'.join([S[i:i+K] for i in range(0, len(S), K)])[::-1]
