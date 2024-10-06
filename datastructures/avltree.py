from __future__ import annotations
from datastructures.iavltree import IAVLTree, K, V
from typing import Generic, Callable, List, Optional, Sequence, Tuple
from collections import deque



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
        if node == None:
            return None

        elif node.balance() > 1:
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
        node = self.searcher(key=key, node=self.root)
        return None if node == None else node.value

    def searcher(self, key: K, node: AVLNode) -> Optional[AVLNode]:
        if node == None:
            return None
        if node.key == key:
            return node.value
        if node.key < key:
            return self.searcher(node.right)
        if node.key > key:
            return self.searcher(node.left)

    def delete(self, key: K) -> None: 
        self.root = self.delete_helper(self.root, key)
        return None

    def delete_helper(self, node: AVLNode, key: K) -> AVLNode:
        if node == None:
            return None
        if key < node.key:
            node.left = self.delete_helper(node.left, key)
        elif key > node.key:
            node.right = self.delete_helper(node.right, key)
        elif key == node.key:
            successor = self.find_successor(node.right)
            if successor == None:
                node =
            node.key = successor.key
            node.value = successor.value
            node.right = self.delete_helper(node=node.right,key=successor.key)

        if node != None:
            node.update_height()
            return self.balance_tree(node=node)
        else:
            return None

    def find_successor(self, node: AVLNode) -> AVLNode:
        if node.left != None and node.right != None:
            current = node.right
            while current.left != None:
                current = current.left
            return current
        else:
            pass

            
            
            # If node is a leaf or has a single child,
            
            #     return node or its child
            
            
            
            # Else #two children - successor will be the smallest node in the right subtree 
            
            
            
            #     Set currrent to node
            
            #     while current.left is not None
            
            #         set current to current.left
            
            #     return current

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
        return self.preorder_helper(self.root)

    def preorder_helper(self, node: AVLNode) -> List[K]:
        sequence = []
        if node != None:
            sequence.append(node.key)
            sequence.extend(self.preorder_helper(node.left))
            sequence.extend(self.preorder_helper(node.right))
        return sequence

    def postorder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        """Returns the postorder traversal of the binary search tree.

        Returns:
            List[K]: The list of keys in postorder traversal.
        """
        return self.postorder_helper(self.root)

    def postorder_helper(self, node:AVLNode) -> List[K]:
        sequence = []
        if node != None:
            sequence.extend(self.postorder_helper(node.left))
            sequence.extend(self.postorder_helper(node.right))
            sequence.append(node.key)
        return sequence

    def bforder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        """Returns the keys in the binary search tree in breadth-first order.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            List[K]: The list of keys in breadth-first order.
        """
        # https://medium.com/@sergioli/breath-first-and-depth-first-search-on-tree-and-graph-in-python-99fd1861893e
        if self.root is None:
            return
        
        queue = deque([self.root])
        sequence = []

        while queue:
            node = queue.popleft()  # dequeue a node from the front of the queue
            sequence.append(node.key)

            # enqueue left child
            if node.left:
                queue.append(node.left)
            # enqueue right child
            if node.right:
                queue.append(node.right)

        return sequence

    def size(self) -> int:
        """Returns the number of nodes in the binary search tree.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            int: The number of nodes in the tree.
        """
        return self.subtree_size(self.root)

    def subtree_size(self, node: AVLNode) -> int:
        left_size = 0 if node.left == None else self.subtree_size(node.left)
        right_size = 0 if node.right == None else self.subtree_size(node.right)
        return 1 + left_size + right_size