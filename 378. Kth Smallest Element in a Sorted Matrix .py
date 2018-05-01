#Solution1 idea: get all the elements and sort them, find the kth largest element
#O(nlogn) in time, close to O(n) since the rows in matrix are partially sorted, O(n ** 2) in space
class Solution1(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        temp = []
        for r in matrix:
            temp.extend(r)
        return sorted(temp)[k-1]


#Solution2 idea: 
#
import heapq

class Solution2(object):
    def kthSmallest(self, matrix, k):
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret