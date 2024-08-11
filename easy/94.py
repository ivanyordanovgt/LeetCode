# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(root):

    result = []

    def inorder(root):

        if not root:
            return

        inorder(root.left)
        inorder(root.right)

        result.append(root.val)

    inorder(root)
    return root


