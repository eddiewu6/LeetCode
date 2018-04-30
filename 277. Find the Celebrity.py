#Create a knownTable to mark each known status of i to j
#Count the known status so find celebrity
#O(n ** 2) in Time and O(n ** 2) in Space
#95/171 Cases passed, 96 failed due to time exceed limit
class Solution1(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        if n == 1:
            return 0
        knownTable = []
        for i in range(n):
            raw = []
            for j in range(n):
                raw.append(knows(i,j))
            knownTable.append(raw)
        
        for i in range(n):
            if knownTable[i].count(False) == n-1:
                if [row[i] for row in knownTable].count(True) == n:
                    return i
        return -1

#Count the known status so find celebrity
#O(n ** 2) in Time and O(1) in Space
#147/171 Cases passed, 148 failed due to time exceed limit
class Solution2(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        if n == 1:
            return 0
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j:
                    if knows(i,j) != knows(j,i):
                        break
                    elif knows(i,j) == False and knows(j,i) == True:
                        count += 1
            if count == n-1:
                return i
        return -1

#
#O(n) in Time and O(1) in Space
#AC


class Solution3(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        possibleCelebrity = 0
        for i in xrange(n):
            if knows(possibleCelebrity, i):
                possibleCelebrity = i
        for i in xrange(possibleCelebrity):
            if knows(possibleCelebrity, i):
                return -1
        for i in xrange(n):
            if not knows(i, possibleCelebrity) :
                return -1
        return possibleCelebrity

        """
        #Wrong solution, which still got AC. Test cases not covered
        
        c = 0
        for i in range(1, n):
            if knows(c, i):
                c = i
        for i in range(c):
            if knows(c, i):
                return -1
        for i in range(c+1, n):    # wrong, should search range(n) except c
            if not knows(i, c):
                return -1
        return c
        """