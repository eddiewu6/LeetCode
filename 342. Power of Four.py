#Solution1 find all power of 4
#
#


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #4**15 = 1073741824 < 2147483647
        table = set({})
        for i in range(16):
            table.add(4**i)
        if num not in table:
            return False
        else:
            return True


#
#
#

class Solution(object):
    def isPowerOfFour(self, num):
        mask = 1431655765
        maxx = 2**31
        
        return num > 0 and maxx%num==0 and mask&num == num
        
        """
        :type num: int
        :rtype: bool
        """
