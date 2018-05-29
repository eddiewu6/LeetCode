#Solution 1, tried to use two pointers, but wrong answer
#Wrong Answer, pass 458/460 cases
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None or s == "":
            return False
        if len(s) <= 2:
            return True
        i = 0
        j = len(s) - 1
        chanceUsed = False
        while i <= j:
            print(s[i],s[j])
            if s[i] != s[j]:
                #Case "lcuucul" makes mistake here
                if s[i+1] == s[j] or s[i] == s[j-1]:
                    if s[i+1] == s[j] and chanceUsed == False:
                        i += 1
                        chanceUsed = True
                    elif s[i] == s[j-1] and chanceUsed == False:
                        j -= 1
                        chanceUsed = True
                    else:
                        return False
                else:
                    return False
            i += 1
            j -= 1
        return True

#Solution2, idea two pointers to remove the different element, and check the rest
#O(n) in time, O(1) in space 
#AC in 115ms

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None or s == "":
            return False
        if len(s) <= 2:
            return True
        
        if self.checkPalindrome(s):
            return True
        else:
            i = -1
            j = len(s)
            while i<=j:
                i += 1
                j -= 1
                if s[i] != s[j]:
                    break
            return self.checkPalindrome(s[:i]+s[i+1:]) or self.checkPalindrome(s[:j]+s[j+1:])
        
        
    def checkPalindrome(self,s):
        if len(s) % 2 == 0:
            return s[:len(s)/2] == s[len(s)/2:][::-1]
        else:
            return s[:len(s)/2] == s[len(s)/2+1:][::-1]