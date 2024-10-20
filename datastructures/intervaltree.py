from datastructures.avltree import AVLTree, AVLNode

class IntervalNode:
    def __init__(self, low: int, high: int, symbol):
        self.low = low
        self.high = high
        self.symbol = symbol
        self.left = None
        self.right = None
        self.height = 1
        self.max = high
    
    def balance(self):
        L = 0 if self.left == None else self.left.height
        R = 0 if self.right == None else self.right.height
        return L - R

    def adjust_height(self):
        self.height = max(
            0 if self.right == None else self.right.height, 
            0 if self.left == None else self.left.height,
        ) + 1

    def update_max(self):
        if self.right == None:
            self.max = self.high
        else:
            self.update_max(self.right)
            self.max = max(self.high, self.right.max)

class IntervalTree:
    # i hate thissss
    def __init__(self):
        self.root = None

    def insert(self, low: int, high: int, symbol):
        self.root = self.insert_helper(low=low, high=high, symbol=symbol, node=self.root)

    def insert_helper(self, low: int, high: int, symbol, node: IntervalNode):
        if low >= node.low:
            node = self.insert_helper(low=low, high=high, symbol=symbol, node=node.right)
        else:
            node = self.insert_helper(low=low, high=high, symbol=symbol, node=node.left)
        node.adjust_height()
        node.update_max()
        node = self.balance_tree(node=node)
        return node

    def balance_tree(self, node: IntervalNode):

