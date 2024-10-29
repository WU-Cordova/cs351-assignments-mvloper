from __future__ import annotations
from typing import Generic, Callable, List, Optional, Sequence, Tuple
# from collections import deque
from dataclasses import dataclass
from datastructures.avltree import AVLTree, AVLNode
import numpy as np


# insert is not working properly
# search is not working properly


@dataclass
class IntervalNode(AVLNode):
    key: int 
    value: dict
    maxend: int
    height: int = 1
    right: Optional[IntervalNode] = None
    left: Optional[IntervalNode] = None

    def update_max_end(self):
        highs = [x for x in self.value]
        self.maxend = max(
            0 if self.left == None else self.left.maxend,
            0 if self.right == None else self.right.maxend,
            max(highs)
            )


class IntervalTree(AVLTree):
    def __init__(self):
        self.root = None
    
    def interval_insert(self, high: int, low: int, data) -> None:
        self.root = self.interval_insert_helper(high=high, low=low, data=data, node=self.root)
    
    def interval_insert_helper(self, high: int, low: int, node: IntervalNode, data) -> IntervalNode:
        if node == None:
            return IntervalNode(key=low, value={high:data}, maxend=high)
        elif node.key == low:
            node.value[high] = data
            node.maxend = max(node.maxend, high)
        elif node.key < low:
            node.right = self.interval_insert_helper(low=low, high=high, data=data, node=node.right)
        elif node.key > low:
            node.left = self.interval_insert_helper(low=low, high=high, data=data, node=node.left)
        node.update_max_end()
        node.update_height()
        return self.balance_tree(node=node)
    
    def balance_tree(self, node: IntervalNode):
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
    
    def rotate_left(self, node: IntervalNode) -> IntervalNode:
        new_root = node.right
        new_left_subtree = new_root.left
        node.right = new_left_subtree
        new_root.left = node

        node.update_height()
        new_root.update_height()

        return new_root

    def rotate_right(self, node: IntervalNode) -> IntervalNode:
        new_root = node.left
        new_right_subtree = new_root.right
        node.left = new_right_subtree
        new_root.right = node

        node.update_height()
        new_root.update_height()

        return new_root
    
    def search(self, point: int):
        return self.intervals_at(point=point, node=self.root)
    
    def intervals_at(self, point: int, node: IntervalNode) -> List:
        current_list = []
        if node == None:
            return current_list
        if node.maxend < point:
            return current_list
        
        if node.key > point:
            current_list.extend(self.intervals_at(point=point, node=node.left))

        if  node.key <= point:
            for high in node.value:
                if high >= point:
                    current_list.append(node.value[high])
            current_list.extend(self.intervals_at(point=point, node=node.right))
            current_list.extend(self.intervals_at(point=point, node=node.left))
        
        return current_list
    
    def size(self) -> int:
        """Returns the number of nodes in the binary search tree.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            int: The number of nodes in the tree.
        """
        return self.subtree_size(self.root)

    def subtree_size(self, node: IntervalNode) -> int:
        left_size = 0 if node.left == None else self.subtree_size(node.left)
        right_size = 0 if node.right == None else self.subtree_size(node.right)
        return 1 + left_size + right_size