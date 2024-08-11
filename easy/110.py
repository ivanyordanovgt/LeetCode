from utils.list_to_node import listToTreeNode


def isBalanced(root):
    if not root:
        return True

    def findBalance(node):
        if not node:
            return True, 0

        left_balanced, left_hight = findBalance(node.left)
        right_balanced, right_hight = findBalance(node.right)

        height = 1 + max(left_hight, right_hight)
        balanced = (left_balanced and right_balanced) and abs(left_hight - right_hight) <= 1

        return balanced, height
    is_balanced, height = findBalance(root)

    return is_balanced


input = listToTreeNode([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
result = isBalanced(input)
print(result)
