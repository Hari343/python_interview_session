from .data_structures import TreeNode
from typing import List, Any
from collections import deque


def to_tree(arr: List[int]) -> TreeNode:
    """
    This function will take a list integers and convert it to a binary tree in-order
    :param arr:
    :return:
    """

    values = iter(arr)
    root = TreeNode(next(values))
    nodes_to_add = deque()
    nodes_to_add.append(root)

    try:
        while True:
            next_node = nodes_to_add.popleft()

            new_left = next(values)
            if new_left is not None:
                next_node.left = TreeNode(new_left)
                nodes_to_add.append(next_node.left)

            new_right = next(values)
            if new_right is not None:
                next_node.right = TreeNode(new_right)
                nodes_to_add.append(next_node.right)

    except StopIteration:
        return root




