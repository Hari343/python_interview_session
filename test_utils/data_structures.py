
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if self.val != other.val:
            return False

        return (self.left == other.left) and (self.right == other.right)



