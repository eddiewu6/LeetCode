#Idea
#O(n) in time, O(n) in space
#AC in 55ms 


class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        #Scover is a mask to deal with the example situation
        Scover = [False]*len(S)
        for i in range(len(words)):
            start = S.find(words[i])#find function only return the first matching element's index
            end = len(words[i]) + start
            while start > -1:
                for j in range(start,end):
                    Scover[j] = True
                start = S.find(words[i],start+1)
                end = len(words[i]) + start
        
        res = ""
        i = 0
        while i < len(S):
            if Scover[i] == True:
                #i is start
                j = i
                while j < len(S) and Scover[j] == True:
                    j += 1
                #j is end
                res = res + "<b>" + S[i:j] + "</b>"
                i = j
                
            else:
                res = res + S[i]
                i += 1
        return res
            