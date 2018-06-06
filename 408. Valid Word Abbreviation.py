#idea:make comparison
#O(n) in time，O(1) in space
#AC in 44ms 


class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if word == None and abbr != None:
            return False
        if word != None and abbr == None:
            return False
        if word == None and abbr == None:
            return True
        
        curletter = 0
        i = 0
        while i < len(abbr) or curletter < len(word):
            
            if i >= len(abbr) or curletter >= len(word):
                return False
            
            if abbr[i].isalpha():
                if abbr[i] != word[curletter]:
                    return False
                i += 1
                curletter += 1
            
            elif abbr[i].isdecimal():
                if abbr[i] != "0":#for case "a" "01"
                    numS = ""
                    while i < len(abbr) and abbr[i].isdecimal():
                        numS = numS + abbr[i]
                        i += 1
                    num = int(numS)
                    #print(num)
                    if num + curletter > len(word):
                        return False
                    if i == len(abbr) and num + curletter < len(word):
                        return False
                    curletter += num
                else:
                   return False
        return True