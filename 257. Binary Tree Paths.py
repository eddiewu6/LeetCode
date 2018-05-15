#Idea: DFS to find the leaf and generate out put. The solution below is DFS with stack
#O(n) in time, O(log(n)) in space
#AC in 48ms


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        
        res = [] #Used for store the result root-to-root paths
        paths = [[root]] #Used as a stack to store the path from root, and implement dfs
        while len(paths) != 0:
            curPath = paths[0] #first path in the paths stack
            cur = paths[0][-1] #the end node of that path
            paths = paths[1:] #pop the path in the stack
            
            #if the end node has left, append it to the path, and append that path to the paths stack
            if cur.left != None:
                #Here, the curPath has to be cloned, you cannot use thisPath = curPath, since it will make thisPath point to
                #the same address of curPath. Any operation done on thisPath will have influence on curPath
                thisPath = curPath[:]
                thisPath.append(cur.left)
                paths.append(thisPath)
            #if the end node has right, append it to the path, and append that path to the paths stack
            if cur.right != None:
                thisPath = curPath[:]
                thisPath.append(cur.right)
                paths.append(thisPath)
            #if the end node has no left or right, this is a leaf node. Generate a result
            if cur.left == None and cur.right == None:
                path = ""
                for i in curPath:
                    path =path+str(i.val)+"->"
                res.append(path[:len(path)-2:]) # len(path)-2 is because there will always be an extra "->" at the end
        return res