#Bubble sort
#O(n ** 2) in time, O(1) in space

def bubbleSort(nums):

	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			if nums[i] > nums[j]:
				nums[i],nums[j] = nums[j], nums[i]
	return nums

nums = [4,3,5,1,2,4,2,7]
print(bubbleSort(nums))

