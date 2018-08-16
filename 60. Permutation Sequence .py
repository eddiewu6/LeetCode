#Recursively to find each digits according to new k and n
#


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        self.digits = [] #track used and unused digits
        self.total = 1 #track how many posibilities there are
        self.result = "" #result

        for i in range(1,n+1):
            self.digits.append(i)
            self.total = i*self.total

        self.recursive(n,k-1)
        return self.result
        
    def recursive(self,newN,newK):
        if newN == 1:
            self.result += str(self.digits[0])
            self.digits[0] = 10
        else:
            self.total = self.total / newN
            index = int(newK /self.total)
            self.result += str(self.digits[index])
            self.digits[index] = 10
            self.digits.sort()
            self.recursive(newN-1,newK-index*self.total)