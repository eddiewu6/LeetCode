# Idea: use hashtable to remove duplicates and the ascii number of each letter
#O(n) in time, O(1) in space
#AC in 40ms


class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        minmax = ord(target)
        letters = dict().fromkeys(letters)
        for i in letters.keys():
            letters[i] = ord(i)
        for i in range(1,26):
            #find the minimum letter by increasing i
            if chr(minmax+i) in letters.keys():
                return chr(minmax+i)
            #If i has reached the end of the alphabtical, return the minimum letter in letters
            if i == 25:
                return chr(min(letters.values()))
        