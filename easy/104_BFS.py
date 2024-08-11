from collections import deque


def maxDepth(root):
    if not root:
        return 0

    stack = deque([root])
    level = 0
    while stack:
        for i in range(len(stack)):
            node = stack.popleft()

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        level += 1

    return level
