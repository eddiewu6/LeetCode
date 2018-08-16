#Iead: calculate how many times each digit needs to shift by mod 26,reduce the time consumption to O(n) by introduce a total number
#O(n) in time, O(1) in space
#AC in 76ms beat 98.88%



class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        if S == None:
            return S

        total = 0
        for i in range(len(shifts)):
            shifts[i] = shifts[i] % 26
            total += shifts[i]
        for i in range(len(shifts)):
            temp = shifts[i]
            shifts[i] = total % 26
            total -= temp
        
        S = list(S)
        for i in range(len(S)):
            S[i] = chr((ord(S[i]) + shifts[i] - ord('a')) % 26 + ord('a'))
        S = "".join(S)
        return S


