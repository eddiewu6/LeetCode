#idea
#
#AC in 105ms



class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.cur = -1#current pointer
        self.len = 0#current length of the whole string
        self.letter = ""#letter dictionary
        self.letterCount = []#letter counts dictionary
        i = 0
        while i < len(compressedString):
            if compressedString[i].isalpha():
                self.letter = self.letter + compressedString[i]
                i += 1
            else:
                temp = ""
                #incase the compressedString has "a100n2000"
                while i < len(compressedString) and compressedString[i].isdigit():
                    temp = temp + compressedString[i]
                    i += 1 
                self.letterCount.append(int(temp))
                self.len += int(temp)
        

    def next(self):
        """
        :rtype: str
        """
        self.cur += 1
        j = self.cur
        if self.hasNext():
            for i in range(len(self.letterCount)):
                j = j - self.letterCount[i]
                if j < 0:
                    return self.letter[i]
        #reach to the last letter    
        elif self.hasNext() == False and self.cur == self.len - 1:
            return self.letter[-1]
        else:
            #print("empty",self.cur)
            return " "

    def hasNext(self):
        """
        :rtype: bool
        """
        #print(self.cur)
        if self.cur >= self.len-1:
            return False
        return True
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()