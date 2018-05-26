#Use hashtable to store the index of elements in nums
#O(n) in time, O(n) in space
#AC in 69ms

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == [] or nums == None or len(nums) == 1 or k <= 0:
            return False
        hashTable = {}#key is num in nums, value is its index in nums
        """
        The enumerate() function adds a counter to an iterable.

        So for each element in cursor, a tuple is produced with (counter, element); the for loop binds that to row_number and row, respectively.
        """
        for i, num in enumerate(nums):
            if num in hashTable and i - hashTable[num] <= k:
                return True
            hashTable[num] = i
        return False