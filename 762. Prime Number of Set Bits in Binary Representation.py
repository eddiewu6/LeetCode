#Solution idea, find how many set bits for each number, and judge whether it is prime, since R is less than
#10^6, so set bit should be less than 2 ** 17. Prime less or eaqual than 17 is not much
#O(n) in time, with O(n) in space
#AC in 416ms

class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count = [0]*(R-L+1)
        for i in range(len(count)):
            count[i] = str(bin(L+i)).count("1")
            if count[i] % 2 == 0 and count[i] != 2:
                count[i] = 0
                continue
            if count[i] % 3 == 0 and count[i] != 3:
                count[i] = 0
                continue
            if count[i] % 5 == 0 and count[i] != 5:
                count[i] = 0
                continue
            if count[i] % 7 == 0 and count[i] != 7:
                count[i] = 0
                continue
            if count[i] % 11 == 0 and count[i] != 11:
                count[i] = 0
                continue
            if count[i] % 13 == 0 and count[i] != 13:
                count[i] = 0
                continue
            if count[i]%17 == 0 and count[i] != 17:
                count[i] = 0
                continue
            
            if count[i] == 1:
                count[i] = 0
                continue
                
        #print(count)
        return len(count)-count.count(0)