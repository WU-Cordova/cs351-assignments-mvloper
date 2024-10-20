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
            node: IntervalNode,
            ) -> IntervalNode:

        if node == None:
            node = IntervalNode(low=low)
            node.intervals_at_low.insert(key=high, value=value)
        else:
            if node.low < low:
                self.insert_helper(
                    low=low, 
                    high=high, 
                    value=value, 
                    node=node.right,
                )
            elif node.low > low:
                self.insert_helper(
                    low=low, 
                    high=high, 
                    value=value, 
                    node=node.left,
                )
            elif node.low == low:
                # insert new node into AVLTree at low
                node.intervals_at_low.insert(key=high, value=value)

        return self.balance_tree(node).update_height()

    def search(self, key=int):
        return self.searcher_helper(key=key, node=self.root)

    def searcher_helper(self, key: int, node: IntervalNode):
        if node.low > key:
            return self.searcher_helper(key=key, node=node.left)
        else:
            if node.right.low < key:
                return self.searcher_helper(key=key, node=)