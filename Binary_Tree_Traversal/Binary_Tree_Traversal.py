"""
Binary tree traversals
"""
# Pre-order traversal
def pre_order(node):
    """
    Returns list of nodes in pre-order
    """
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)


# In-order traversal
def in_order(node):
    """
    Returns list of nodes in in-order
    """
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)

# Post-order traversal
def post_order(node):
    """
    Returns list of nodes in post-order
    """
    if node is None:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]
