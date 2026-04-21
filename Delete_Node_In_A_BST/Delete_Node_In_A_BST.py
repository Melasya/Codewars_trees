"""
Module for deleting node
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    """
    Binary tree node class
    """
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes binary tree nodes
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Class representing solution
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Deletes the node with the given key in the BST
        """
        if root is None:
            return None

        #search
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        #deleting
        if root.right is None and root.left is None:
            return None
        if root.right is None:
            return root.left
        if root.left is None:
            return root.right

        successor = root.right
        while successor.left is not None:
            successor = successor.left
        root.val = successor.val
        root.right = self.deleteNode(root.right, successor.val)
        return root
