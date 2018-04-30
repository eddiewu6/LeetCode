#Idea: binary search for the citation times in citations that is less than n-mid
#O(logn) in Time, O(1) in space

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        n = len(citations)
        i, j = 0, n - 1
        while i <= j:
            mid = (i+j)/2
            if citations[mid] < n-mid: 
                i = mid + 1
            else: 
                j = mid - 1
        return n-i