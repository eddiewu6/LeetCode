#BFS with queue
#O(n ** 2) in time, O(m * n) in space
#AC in 391ms

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if graph == None or len(graph) == 0:
            return []
        stack = [[0]]
        res = []
        while len(stack) > 0:
            cur = stack[0]
            stack = stack[1:]
            for i in graph[cur[-1]]:
                #get rid of circle
                if i not in cur:
                    temp = cur[:]
                    temp.append(i)
                    #Final destination reached
                    if i != len(graph)-1:
                        stack.append(temp)
                    else:
                        res.append(temp)
        return res

		
#DFS with stack
#O(n ** 2) in time, O(m * n) in space
#AC in 391ms	
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if graph == None or len(graph) == 0:
            return []
        stack = [[0]]
        res = []
        while len(stack) > 0:
            cur = stack.pop()
            for i in graph[cur[-1]]:
                #get rid of circle
                if i not in cur:
                    temp = cur[:]
                    temp.append(i)
                    #Final destination reached
                    if i != len(graph)-1:
                        stack.append(temp)
                    else:
                        res.append(temp)
        return res
