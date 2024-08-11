class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):

    def recursive(node, node2):
        if not node and not node2:
            return True

        if not node or not node2 or node.val != node2.val:
            return False

        return recursive(node.left, node2.left) and recursive(node.right, node2.right)

    return recursive(p, q)

