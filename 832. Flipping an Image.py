#Strage forward solution
#O(n ** 2) in time, O(1) in space
#AC in 73ms

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if A == None or A == []:
            return A
        
        for i in range(len(A)):
            A[i] = A[i][::-1]
            A[i] = map(lambda x: x ^ 1,A[i])
        return A