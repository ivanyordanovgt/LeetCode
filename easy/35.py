def searchInsert(nums, target):

    if target <= nums[0]:
        return 0

    for i in range(0, len(nums)):
        if nums[i] == target:
            return i

        if i - 1 >= 0:
            if target > nums[i - 1] and target < nums[i]:
                return i

    return len(nums)

nums, target = [5, 6, 7, 9], 2
print(searchInsert(nums, target))