#Solution1 Idea: sort the citations, and find the citation time larger than the rest count in the citations array
#O(nlogn) in time, O(1) in space
#AC
class Solution1(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #Sort the citations list
        citations.sort()
        #Exactly following the defination of index h if h of his/her N papers have at least h citations each, 
        #and the other N − h papers have no more than h citations each
        for i in range(len(citations)):
            if citations[i] >= len(citations)-i:
                return len(citations)-i
        #Deal with all 0 citation case
        return 0

#Solution2 Idea:Count how times of each citation
#
#O(n) in time, O(n) in space
#AC
class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        
        n = len(citations)
        papers = [0] * (n + 1)  # papers[i] is the number of papers with i citations.
        for c in citations:
            papers[min(n, c)] += 1  # All papers with citations larger than n is count as n.
            print(papers)
        i = n
        s = papers[n]
        while i > s:
            i -= 1
            s += papers[i]
        return i