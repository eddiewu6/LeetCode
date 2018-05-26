#Idea:
#O(n ** 2) in time, O(1) in space
#AC in 1082ms

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s == None or s == "":
            return True
        if len(s) == 1:
            return False
        #check s[0:1],s[0:2],s[0:3] ... s[0:len(s)/2] can form partial of the s in a repeated way
        i = 1
        while i < len(s) / 2 + 1:
            target = s[:i]
            j = 0
            #Check whether the parten is same as target
            while j < len(s):
                if s[j:j+i] != target:
                    #if it is not the same, increase i by 1
                    i += 1
                    break
                else:
                    j += i
            #if j reach the end, it means that all previous str has same paten
            if j == len(s):
                return True
        return False