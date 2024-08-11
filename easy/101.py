def isSymmetric(root):
    left, right = root.left, root.right

    def recursive(l, r):

        if not l and not r:
            return True

        elif not l or not r or l.val != r.val:
            return False

        return recursive(l.left, r.right) and recursive(l.right, r.left)

    return recursive(left, right)
