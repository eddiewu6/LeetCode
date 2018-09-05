#Selection_sort
#O(n ** 2) in time, O(1) in space

def slectionSort(nums):

	for i in range(len(nums) - 1):
		
		minIndex = i
		
		for j in range(i,len(nums)):

			if nums[minIndex] > nums[j]:
				minIndex = j

		nums[minIndex],nums[i] = nums[i],nums[minIndex]

	return nums


nums = [4,3,5,1,2,4,2,7]
print(slectionSort(nums))

