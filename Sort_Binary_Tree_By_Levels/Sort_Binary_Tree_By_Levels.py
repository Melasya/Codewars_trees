class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
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
