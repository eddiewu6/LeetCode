#
#O(n) in time, O(n) in space
#AC in 32ms


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num = str(num)
        reverse = ['0']*len(num)
        for i in range(len(num)):
            reverse[len(num)-1-i] = self.convertDigit(num[i])
            if reverse[len(num)-1-i] == None:
                return False
        reverse = "".join(reverse)
        #print(reverse,num)
        if reverse == num:
            return True
        else:
            return False
            
        
        
        
    def convertDigit(self,dig):
        if dig in ["0","1","8"]:
            return dig
        if dig == "6":
            return "9"
        if dig == "9":
            return "6"
        if dig in ["2","3","4","5","7"]:
            return None