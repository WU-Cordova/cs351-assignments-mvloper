from __future__ import annotations
from datastructures.iavltree import IAVLTree, K, V
from typing import Generic, Callable, List, Optional, Sequence, Tuple



# @dataclass
class AVLNode(Generic[K, V]):
    def __init__(self, key: K, value: V, left: Optional[AVLNode]=None, right: Optional[AVLNode]=None):
      self.key = key
      self.value = value
      self.left = left
      self.right = right
      self.height = 1

    def balance(self) -> int:
        L = 0 if self.left == None else self.left.height
        R = 0 if self.right == None else self.right.height
        return L - R

    def update_height(self) -> int:
        self.height = 1 + max(
            0 if self.left == None else self.left.height,
            0 if self.right == None else self.right.height
        )
        return self.height

# height = max(left.height, right.height) + 1
# balance = left.height - right.height


class AVLTree(IAVLTree[K, V], Generic[K,V]):

    def __init__(self, starting_sequence: Optional[Sequence[Tuple]]=None):
        self.root = None
        if starting_sequence is not None:
            for key, value in starting_sequence:
                self.insert(key, value)

    def insert(self, key: K, value: V) -> None:
        """Inserts a key-value pair into the binary search tree.

            Args:
                key (K): The key used to order the nodes in the tree.
                value (V): The value associated with the key.
        """
        self.root = self.insert_helper(key=key, value=value, node=self.root)
        return

    def insert_helper(self, key: K, value: V, node: AVLNode) -> AVLNode:
        if node is None:
            return AVLNode(key=key, value=value)
        elif key < node.key:
            node.left = self.insert_helper(key=key, value=value, node=node.left)
        else:
            node.right = self.insert_helper(key=key, value=value, node=node.right)

        node.update_height()

        return self.balance_tree(node=node)

    def balance_tree(self, node: AVLNode) -> AVLNode:
        if node.balance() > 1:
            if node.left.balance() < 0:
                node.left = self.rotate_left(node.left)
            node = self.rotate_right(node)

        elif node.balance() < -1:
            if node.right.balance() > 0:
                node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)

        return node

    def rotate_left(self, node: AVLNode) -> AVLNode:
        new_root = node.right
        new_left_subtree = new_root.left
        node.right = new_left_subtree
        new_root.left = node

        node.update_height()
        new_root.update_height()

        return new_root

    def rotate_right(self, node:AVLNode) -> AVLNode:
        new_root = node.left
        new_right_subtree = new_root.right
        node.left = new_right_subtree
        new_root.right = node

        node.update_height()
        new_root.update_height()

        return new_root
        
    
    def search(self, key: K) -> Optional[V]:
        """Searches for a key in the binary search tree and returns the associated value if found.

        Args:
            key (K): The key to search for.

        Returns:
            Optional[V]: The value associated with the key if found, or None if the key is not present.
        """
        return

    def delete(self, key: K) -> None:
        """Deletes a key and its associated value from the binary search tree.

        Args:
            key (K): The key to delete.

        Raises:
            KeyError: If the key is not present in the tree.
        """
        

    def inorder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        """Returns the inorder traversal of the binary search tree, containing the keys in sorted order.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            List[K]: The list of keys in inorder traversal.
        """
        return self.inorder_helper(self.root)

    def inorder_helper(self, node:AVLNode) -> List[K]:
        subtree = []
        if node.left != None:
            subtree.extend(
                self.inorder_helper(node.left)
            )
        subtree.append(node.key)
        if node.right != None:
            subtree.extend(
                self.inorder_helper(node.right)
            )
        return subtree

    def preorder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        """Returns the preorder traversal of the binary search tree.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            List[K]: The list of keys in preorder traversal.
        """
        pass

    def postorder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        """Returns the postorder traversal of the binary search tree.

        Returns:
            List[K]: The list of keys in postorder traversal.
        """
        pass

    def bforder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        """Returns the keys in the binary search tree in breadth-first order.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            List[K]: The list of keys in breadth-first order.
        """
        return self.bf_helper(self.root)
    
    def bf_helper(self, node: AVLNode) -> List[K]:
        subtree = [ node.key ]
        subtree.extend(self.bf_helper(node.left))
        subtree.extend(self.bf_helper(node.right))
        return subtree

    def size(self) -> int:
        """Returns the number of nodes in the binary search tree.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            int: The number of nodes in the tree.
        """
        pass