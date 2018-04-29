class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        """
        #Solution1
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        """
        
        """
        #Solution2
        # O(n ** 2) timing issue. Idea is following the example. 33/34 cases passed
        if k == 0 :
            return
        for i in range(k):
            temp = nums[-1]
            print(temp)
            for j in range(len(nums)-1,-1,-1):
                nums[j] = nums[j-1]
            nums[0] = temp
        """
        
        """
        #Solution3 O(n) Space and O(n) Time
        n = []
        for i in range(len(nums)):
            n.append(nums[i])
        for i in range(len(nums)):
            nums[i] = n[(len(nums)-k+i)%(len(nums))]
        """
        
        #Solution4 O(1) Space and O(n) Time
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        
        
        #Solution 5