#Solution idea: use stack and DFS to find all subordinates and add their importance together
#O(n ** 3) in time, O(n) in space
#AC in 263ms

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if len(employees) == 0 or employees == None:
            return 0
        
        totalImp = 0
        for i in employees:
            if i.id == id:
                totalImp += i.importance
                stack = i.subordinates
                while len(stack) != 0:
                    cur = stack[-1]
                    stack = stack[:len(stack)-1]
                    for j in employees:
                        if j.id == cur:
                            totalImp += j.importance
                            stack.extend(j.subordinates)
        return totalImp