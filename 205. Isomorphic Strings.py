#Idea hashtable
#O(n) in time, O(n) in space
#AC in 43ms

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if s == None or s == "":
            return True
        
        table = dict()
        for i in range(len(s)):
            table[t[i]] = s[i]
        #get rid of situation that s == "aa", t == "ab"
        if len(set(table.values())) < len(table.values()):
            return False
        
        for i in range(len(s)):
            if table[t[i]] != s[i]:
                return False
        return True