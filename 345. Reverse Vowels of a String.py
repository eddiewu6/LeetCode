#Idea: two pointer to find the front vowel and tail vowel
#O(n) in time, O(1) in space
#Ac in 75ms

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            while s[i] not in vowels and i < j:
                i += 1
            while s[j] not in vowels and i < j:
                j -= 1
            if s[i] in vowels and s[j] in vowels:
                s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        res = "".join(s)
        return res
