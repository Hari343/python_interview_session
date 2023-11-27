from typing import List, Optional
from test_utils.data_structures import TreeNode
from test_utils.functions import to_tree

"""
    Given the root of a binary tree, invert the tree, and return its root. Note: In the examples given below
    all nodes are printed in-order.

    Examples 1:
    Input: root = [4,2,7,1,3,6,9]   
    Output: [4,7,2,9,6,3,1]
    Explanation: 
    Input Tree
                4
              /   \
             2      7
           /  \    / \ 
          1    3  6   9

    Output Tree
                4
              /   \
             7      2
           /  \    / \ 
          9    6  3   1      

    Example 2:
    Input: root = [1, 2, 3]
    Output: [1, 3, 2]
    Explanation: 
    Input Tree
                1
              /   \
             2      3

    Output Tree
                1
              /   \
             3      2

    Example 3:
    Input: root = None
    Output: None

"""

"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None , right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right
"""


# invert binary tree
def invert_tree(root: TreeNode) -> TreeNode:

    def dfs(root: TreeNode) -> None:
        if root is None:
            return

        dfs(root.left)
        dfs(root.right)

        root.left, root.right = root.right, root.left

    dfs(root)

    return root


# Feel free to test your code. The code you write after this line won't be marked.
if __name__ == "__main__":
    root = to_tree([4, 2, 7, 1, 3, 6, 9])
    solution_root = to_tree([4, 7, 2, 9, 6, 3, 1])
    inverted_root = invert_tree(root)
    assert (inverted_root == solution_root)
    print("Example test case 1 successful")

    # root = to_tree([4, 2, 7, 1, 3, 6, 9])
    # inverted_tree = invert_tree(root)
    # assert (inverted_tree == root)
    # print("Example test case 1 successful")

    # example test case 2
    root = to_tree([1, 2, 3])
    solution_root = to_tree([1, 3, 2])
    inverted_root = invert_tree(root)
    assert (inverted_root == solution_root)
    print("Example test case 2 successful")

    # assert (94 == third_largest([94, 95, 96]))
    # print("Tests passed")
