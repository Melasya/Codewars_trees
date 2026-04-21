"""
Binary tree level-order traversal
"""
class Node:
    """
    Simple binary tree node
    """
    def __init__(self, L, R, n):
        """
        Initializes node
        """
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    """
    Return list of nodes by levels - left to right
    """
    if node is None:
        return []

    queuee = [node]
    result = []
    while queuee:
        node = queuee.pop(0)
        result += [node.value]

        if node.left is not None:
            queuee.append(node.left)

        if node.right is not None:
            queuee.append(node.right)

    return result
