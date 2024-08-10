def merge(nums1, m, nums2, n):
    nums1_len = len(nums1)
    space_taken = 0

    def popped_numbers(nums):
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                return count

    while len(nums2) > 0:

        if space_taken == len(nums1-m):
            space_diff = popped_numbers(nums1)
            if space_diff > 0:
                nums1[0] = nums1[len(nums1)-m]
            else:
                nums2.insert(0, nums1[0])


        if nums1[0] < nums2[0]:
            nums1[len(nums1)-m+space_taken] = nums1[0]
            nums1[0] = 0
        else:
            nums1[len(nums1)-m+space_taken] = nums2[0]
            nums2.pop(0)


input = [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3]
result = merge(*input)
print(result)
