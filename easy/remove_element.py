def removeElement(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    # Return the number of elements not equal to val.
    return k

result = removeElement([3, 2, 2, 3], 3)
print(result)