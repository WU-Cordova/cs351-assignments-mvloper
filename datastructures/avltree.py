from __future__ import annotations
from iavltree import IAVLTree, K, V
from typing import Generic, Callable, List, Optional, Sequence, Tuple



@dataclass
class AVLNode(Generic[K, V]):
   def __init__(self, key: K, value: V, left: Optional[AVLNode]=None, right: Optional[AVLNode]=None):
      self.key = key
      self.value = value
      self.left = left
      self.right = right
      self.height = 1

# height = max(left.height, right.height) + 1
# balance = left.height - right.height


class AVLTree(IAVLTree[K, V], Generic[K,V]):

    def __init__(self, starting_sequence: Optional[Sequence[Tuple]]=None):
        if starting_sequence is not None:
            for key, value in starting_sequence:
                self.insert(key, value)

    def insert(self, key: K, value: V) -> None:
        """Inserts a key-value pair into the binary search tree.

            Args:
                key (K): The key used to order the nodes in the tree.
                value (V): The value associated with the key.
        """
        if tree is empty create new node
        pass
    
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
        pass

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
        pass

    def size(self) -> int:
        """Returns the number of nodes in the binary search tree.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            int: The number of nodes in the tree.
        """
        pass