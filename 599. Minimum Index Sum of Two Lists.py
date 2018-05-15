#Idea: use set to find the intersection, and count the sum of index for each #intersetion item, and find all the minimum ones. Be aware of multiple minimum #sum of indexs
#O(n) in time, O(n) in space
#AC in 120ms


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        intersection = list(set(list1) & set(list2))
        table = dict().fromkeys(intersection)
        minIndex = len(list1) + len(list2)
        res = []
        for i in intersection:
            table[i] = list1.index(i) + list2.index(i)
            if minIndex > table[i]:
                minIndex = table[i]
        for i in table.items():
            if i[1] == minIndex:
                res.append(i[0])
        return res