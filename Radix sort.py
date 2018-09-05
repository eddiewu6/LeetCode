#Radix sort: sort numbers by digits from least significant digit to most significant digit

def radixSort(nums):
	return None



def countSort(nums):
	#nums is number withing range 0 ~ 10, not including 10
	digits = [0]*10
	#Count the number in nums
	for i in range(len(nums)):
		digits[nums[i] % 10] += 1
	#Add the previous coung to each number in digits
	for i in range(1,len(digits)):
		digits[i] += digits[i-1]

	#return variable
	res = [-1]*len(nums)

	for i in range(len(digits)-1,-1,-1):
		if i > 0:
			while digits[i] > digits[i - 1]:
				res[digits[i]-1] = i
				print("res["+str(digits[i]-1)+"] = "+str(i))
				digits[i] -= 1
		elif i == 0:
			while digits[i] > 0:
				res[digits[i]-1] = i
				digits[i] -= 1
	return res
