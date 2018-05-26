#
#O(n) in time, O(1) in space
#AC in 94ms


class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        
        minn = arrays[0][0]
        maxn = arrays[0][-1]
        result = -20001
        for i in range(1, len(arrays)):
            result = max(result, abs(minn-arrays[i][-1]))
            result = max(result, abs(maxn-arrays[i][0]))
            minn = min(arrays[i][0], minn)
            maxn = max(arrays[i][-1], maxn)
        return result