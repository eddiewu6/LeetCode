
def doSort(nums, head, tail):
    if head < tail:
        p = partition(nums,head,tail)
        doSort(nums,head,p-1)
        doSort(nums,p+1,tail)
    return nums


def partition(nums, head, tail):
    pivot = nums[tail]
    i = head
    for j in range(head,tail):
        if nums[j] < pivot:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
    nums[i],nums[tail] = nums[tail],nums[i]
    return i

nums = [4,2,5,4,6,3,3,5,4,26,74,3]
print(doSort(nums,0,len(nums) - 1))
