from collections import deque
from utils.list_to_node import listToTreeNode
def hasPathSum(root, targetSum):

    if not root:
        return 0

    stack = deque([root])
    value_stack = deque([root.val])
    final_values = []

    while stack:

        for i in range(len(stack)):
            node = stack.popleft()
            c_sum = value_stack.popleft()

            if node.left:
                stack.append(node.left)
                value_stack.append(c_sum+node.left.val)
            if node.right:
                stack.append(node.right)
                value_stack.append(c_sum+node.right.val)


            if not node.left and not node.right:
                final_values.append(c_sum)


    return targetSum in final_values

input = listToTreeNode([5,4,8,11,None,13,4,7,2,None,None,None,1])
result = hasPathSum(input, 22)
print(result)
