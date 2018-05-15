#Recursive with in-order transverse
#
#AC in 100ms


class Solution:
    def convertBST(self, root):
        sumRightTree(root,0)
        return root
        

def sumRightTree(rootRight,res):
    if rootRight != None:
        res = sumRightTree(rootRight.right,res)
        res += rootRight.val
        rootRight.val = res
        res = sumRightTree(rootRight.left,res)
    return res  