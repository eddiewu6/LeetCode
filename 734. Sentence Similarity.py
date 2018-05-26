#Idea: create hash table for each word in pairs
#O(n) in time, O(n) in space
#AC in 35ms beat 100%


class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        table = {}
        
        for i in pairs:
            if i[0] not in table:
                table[i[0]] = [i[0]]
            table[i[0]].append(i[1])
            
            if i[1] not in table:
                table[i[1]] = [i[1]]
            table[i[1]].append(i[0])
            
        for i in range(len(words1)):
            if words2[i] != words1[i]:
                if words1[i] not in table.get(words2[i],[]) and words2[i] not in table.get(words1[i],[]):
                    return False
        return True