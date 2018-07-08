#Make the array descending according to its height, move the people according to the k number
#O(nlogn) in time, O(1) in space
#AC in 156ms


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) < 2:
            return people
        people.sort(key = lambda x:x[0],reverse = True)
        
        
        #Deal with the situation [[3,0],[2,2],[2,0],[4,1]]
        #The height has to be descending, but the for the same height, the k number has to be ascending
        #This part is to make sure the k number for the same h, it is ascending
        i = 0
        target = people[0][0]
        while i < len(people):
            count = 0
            while i + count < len(people) and people[i+count][0] == target:
                count += 1
            
            if count > 1:
                people[i:i+count] = sorted(people[i:i+count],key = lambda x:x[1])
            i  = i + count
            if i < len(people):
                target = people[i][0]
            
        #since the people is now in order of descending height, so just move the people according to the k number
        #Insert the ith people according to its k number
        i = 0
        while i < len(people):
            if people[i][1] < i:
                people = self.doSwap(people,i)
            i += 1
        return people
    #Function is used to do the insertion
    def doSwap(self,people,source):
        tail = people[source+1:]
        head = people[:people[source][1]]
        mid = people[people[source][1]:source]
        people = head+[people[source]]+mid+tail
        return people