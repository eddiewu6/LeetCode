#idea
#O(m*n) in time, O(m*n) in space
#AC in 732ms
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if M == None or M == []:
            return M
        res =[]
        for i in range(len(M)):
            temp = []
            for j in range(len(M[0])):
                temp.append(self.calculate(M,i,j))
            res.append(temp)
        return res
        
    
    def calculate(self,M,i,j):
        total = M[i][j]
        count = 1
        if i - 1 > -1 and j - 1 > -1:
            total += M[i-1][j-1]
            count += 1
        if i - 1 > -1 and j + 1 < len(M[0]):
            total += M[i-1][j+1]
            count += 1
        if i + 1 < len(M) and j -1 > -1:
            total += M[i+1][j-1]
            count += 1
        if i + 1 < len(M) and j + 1 <len(M[0]):
            total += M[i+1][j+1]
            count += 1
        if j - 1 > -1:
            total += M[i][j-1]
            count += 1
        if j + 1 < len(M[0]):
            total += M[i][j+1]
            count += 1
        if i - 1 > -1:
            total += M[i-1][j]
            count += 1
        if i + 1 < len(M):
            total += M[i+1][j]
            count += 1
        return int(total/count)