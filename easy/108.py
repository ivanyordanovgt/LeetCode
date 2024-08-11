class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    if not nums:
        return

    middle = len(nums) // 2
    middle_num = nums[middle]
    root = TreeNode(middle_num)

    root.left = sortedArrayToBST(nums[0: middle])
    root.right = sortedArrayToBST(nums[middle + 1::])

    return root
