#Idea hashtable
#O(n) in time, O(n) in space
#AC in 30ms


class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type string: str
        :rtype: bool
        """
        
        strList = string.split(" ")
        
        #Deal with "aba" "ab ab" situation
        if len(pattern) != len(strList):
            return False
        
        
        patternTable = dict().fromkeys(list(pattern),None)
        for i in range(len(pattern)):
            if patternTable[pattern[i]] == None:
                patternTable[pattern[i]] = strList[i]
            elif patternTable[pattern[i]] != strList[i]:
                return False
            
        #Deal with "aabb","ab ab ab ab" situation
        if len(set(patternTable.values())) != len(patternTable.values()):
            return False
        return True