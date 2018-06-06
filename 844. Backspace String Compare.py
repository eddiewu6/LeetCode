#idea use stack
#O(m+n) in time, O(m+n) in space
#Ac in 36ms

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if S == None or S == "":
            return S == T
        elif T == None or T == "":
            return S == T
        sStack = []
        tStack = []
        for i in S:
            if i.isalpha():
                sStack.append(i)
            elif i == "#":
                if len(sStack) > 0:
                    sStack.pop()
        for j in T:
            if j.isalpha():
                tStack.append(j)
            elif j == "#":
                if len(tStack) > 0:
                    tStack.pop()
        return "".join(sStack) == "".join(tStack)