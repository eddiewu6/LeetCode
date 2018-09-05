def mergeSort(nums):

    if len(nums) <= 1:
        return nums

    leftNums = nums[:len(nums) // 2]
    rightNums = nums[len(nums) // 2:]

    leftNums = mergeSort(leftNums)
    rightNums = mergeSort(rightNums)

    return mergeLeftAndRight(leftNums,rightNums)



def mergeLeftAndRight(leftNums,rightNums):
    print(leftNums,rightNums)
    res = []
    i = 0
    j = 0
    while leftNums and rightNums:
        if leftNums[0] < rightNums[0]:
            res.append(leftNums[0])
            leftNums = leftNums[1:]
        else:
            res.append(rightNums[0])
            rightNums = rightNums[1:]

    res += leftNums
    res += rightNums

    print("res:",str(res))
    return res


nums = [1,4,6,3,65,4,4,6,3,2,1]
print(mergeSort(nums))
