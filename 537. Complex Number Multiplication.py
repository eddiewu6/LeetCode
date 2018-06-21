#Easy with string
#O(1) time, O(1) space
#AC in 36ms



class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        self.readComplex(a,b)
        return self.complexMultiply(self.alist,self.blist)
    
    def readComplex(self,a,b):
        self.alist = a.split("+")
        self.blist = b.split("+")
        self.alist[0] = int(self.alist[0])
        self.alist[1] = int(self.alist[1][:len(self.alist[1])-1])
        self.blist[0] = int(self.blist[0])
        self.blist[1] = int(self.blist[1][:len(self.blist[1])-1])
        
    def complexMultiply(self,alist,blist):
        res = [0,0]
        res[0] = alist[0]*blist[0] - alist[1]*blist[1]
        res[1] = alist[0]*blist[1] + blist[0]*alist[1]
        resString = "".join([str(res[0]),"+",str(res[1]),"i"])
        return resString