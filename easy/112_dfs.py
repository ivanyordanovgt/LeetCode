from collections import deque
from utils.list_to_node import listToTreeNode


def hasPathSum(root, targetSum):
    if not root:
        return 0

    def dfs(node, total_sum):
        if not node:
            return False

        total_sum += node.val

        if not node.left and not node.right:
            return total_sum == targetSum

        return dfs(node.left, total_sum) or dfs(node.right, total_sum)

    return dfs(root, 0)


input = listToTreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
result = hasPathSum(input, 22)
print(result)
