from collections import deque
from utils.list_to_node import listToTreeNode

def minDepth(root):
    if not root:
        return 0

    stack = deque([root])
    level = 1
    while stack:

        for i in range(len(stack)):
            node = stack.popleft()

            if not node:
                break

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            if not node.left and not node.right:
                return level

        level += 1

    return level

input = listToTreeNode([2,None,3,None,4,None,5,None,6])
result = minDepth(input)
print(result)