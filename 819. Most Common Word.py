#Solution idea: in lines
#O(n) in time, O(n) in space
#AC in 36ms

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        #make all case lower
        paragraph = paragraph.lower()
        #remove symbols
        symbols = ["!","?","\'",",",";","."]
        for i in symbols:
            paragraph = paragraph.replace(i,"")
        #split with space
        words = paragraph.split(" ")
        
        #Use hashtable to count the presenting times.
        #Time complexity for dict.fromkeys() is O(n), since for dictionary, i in #dict() is O(1), and dict().set is O(1), these all execute n times.
        countDic = dict().fromkeys(words,0)
        for i in countDic.keys():
            if i not in banned:
                countDic[i] = words.count(i)
        #find max count word
        mostword = ""
        maxtimes = 0
        for i in countDic.keys():
            if countDic[i] > maxtimes:
                maxtimes = countDic[i]
                mostword = i
        return mostword