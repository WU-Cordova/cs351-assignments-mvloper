from __future__ import annotations

from typing import Tuple, Any, Optional
from datastructures.avltree import AVLTree, AVLNode

class IntervalNode(AVLNode):
    def __init__(
            self, 
            low: int, 
            intervals_at_low: AVLTree = AVLTree(), 
        ):
        self.low = low
        self.intervals_at_low = intervals_at_low
        self.left = None
        self.right = None
        self.height = 1


class IntervalTree(AVLTree):
    def __init__(self):
        self.root = None

    def insert(
            self, 
            low: int, 
            high: int, 
            value, 
        ) -> None:
        self.root = self.insert_helper(low, high, value, self.root)
        return

    def insert_helper(
            self, 
            low: int, 
            high: int, 
            value, 
            node: IntervalNode
        ) -> IntervalNode:

        if node == None:
            node = IntervalNode(
                low=low, 
                intervals_at_low=AVLTree(
                    starting_sequence=[(high, value)]
                    )
                )
            
        else:
            if node.low < low:
                self.insert_helper(low, high, value, node.right)
            elif node.low > low:
                self.insert_helper(low, high, value, node.left)
            elif node.low == low:
                # insert new node into AVLTree at low
                node.intervals_at_low.insert(high, value)

        return self.balance_tree(node).update_height()


    # def search(self):
