#Use hashtable with distance to each point as keys, and count of the points to current point has this 
#distance as value.
#O(n**2) in time, O(n) in space
#AC in 1664 ms

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        #dis = []
        for i in points:
            table = dict()
            for j in points:
                if i != j:
                    distance = (i[0]-j[0]) ** 2 + (i[1]-j[1]) ** 2
                    if distance in table.keys():
                        table[distance] += 1
                    else:
                        table.setdefault(distance,1)
            for k in table.keys():
                #If only 1 point to i has k's distance, it will return 0
                #If 2 points to i has k'2 distance, it will return 2, since there are 2 kinds of orders
                #If 3 points, return 6, since 6 different kinds of orders and combination
                res += table[k] * (table[k]-1)     
        return res