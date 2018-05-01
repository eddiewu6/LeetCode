#Solution idea
#O(n) in time, O(1) in space
#AC in 36ms

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 1
        carry = int((digits[-1]+num) / 10)
        digits[-1] = int((digits[-1]+num) % 10)
        if carry == 0:
            return digits
        else:
            for i in range(len(digits)-2,-1,-1):
                if carry == 0:
                    break
                t = digits[i]+carry
                digits[i] = t % 10
                carry = int(t / 10)
            if carry == 1:
                return [1]+digits
            else:
                return digits