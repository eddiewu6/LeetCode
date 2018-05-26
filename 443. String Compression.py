#slow pointer and fast pointer
#O(n) in time, and O(1) in space
#AC in 92ms

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 0 or len(chars) == 1:
            return len(chars)
        
        res = 0 #current result for the length of chars
        i = 0 #slow pointer
        
        while i < len(chars):
            target = chars[i]
            j = i + 1
            
            #increase the fast pointer if the following char[j] is same as target
            while j < len(chars) and chars[j] == target:
                j += 1
            
            targetCount = list(str(j - i)) # count of target
            
            if targetCount != ["1"]:#if count of target is not 1
                for k in range(len(targetCount)):# change the array in place according to the length of targetCount
                    chars[res+1+k] = targetCount[k]
                res = res + 1 + len(targetCount) # increase the result by len(targetCount)
            elif targetCount == ["1"]:
                res = res + 1# no need to change the chars array, just increase the res by 1
            i = j#set the slow pointer to j to check next target
            if i < len(chars):# make current res position as next target
                chars[res] = chars[i]
        return res
                
                    