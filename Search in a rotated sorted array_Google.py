
#O(nLogn) solution is to sort the array again and find the solution
#O(Logn) is achievable since it is partially sorted array, which we can make use of.

#O(Logn) in time, O(1) in space

class Solution:
	def searchInRotatedArray(self,nums,target):
		#Boundary check
		if len(nums) == 0 or nums == None:
			return -1

		left = 0
		right = len(nums) - 1

		#Binary search with extra condition check of the target range
		while left <= right:

			mid = (left + right) / 2
			if target == nums[mid]:
				return mid

			if nums[low] <= nums[mid]:
				if nums[left] <= target and target <= nums[mid]:
					right = mid - 1
				else:
					left = mid + 1
			else:
				if nums[mid] <= target and target <= nums[right]:
					left = mid + 1
				else:
					right = mid - 1

		return -1



