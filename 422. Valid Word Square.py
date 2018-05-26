#Idea:check whether the matrix is sematric to its interval
#O(n ** 2) in time, O(1) in space
#AC in 52ms

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        
        if words == None:
            return False
        #make the short row as long as the colomn number
        for i in range(len(words)):
            words[i] = words[i]+" "*(len(words)-len(words[i]))
        #check whether row count is same as colomn count, if not return False
        for i in range(len(words)):
            if len(words) != len(words[i]):
                return False
        #compare whether the square is sysmatric to its interval
        for i in range(len(words)):
            for j in range(i):
                if words[i][j] != words[j][i]:
                    return False
        return True