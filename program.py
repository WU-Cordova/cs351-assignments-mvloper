from datastructures.avltree import AVLTree, AVLNode
import random
from collections import deque

sequence0 = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]
sequence1 = [i for i in sequence0]
sequence = []

for i in range(len(sequence0)):
    x = random.choice(sequence0)
    sequence.append(x)
    sequence0.remove(x)

print(sequence)
print(sequence1, "\n")

tree = AVLTree(starting_sequence=sequence)
tree1 = AVLTree(starting_sequence=sequence1)

print("inorder", tree.inorder(), "   ", tree1.inorder())
print("bforder", tree.bforder(), "   ", tree1.inorder())
print("preorder", tree.preorder(), "   ", tree1.inorder())
print("postorder", tree.postorder(), "   ", tree1.inorder())

assert(tree.inorder() == tree1.inorder())
assert(tree.bforder() == tree1.bforder())
assert(tree.preorder() == tree1.preorder())
assert(tree.postorder() == tree1.postorder())

# print(f"     {tree.root.key}")
# print(f"   /   \\")
# print(f"  {tree.root.left.key}     {tree.root.right.key}")
# print(f" / \\   / \\")
# print(f"{tree.root.left.left.key}   {tree.root.left.right.key} {tree.root.right.left.key}   {tree.root.right.right.key}")
# print("\n")

# tree.insert(key=7,value=7)

# print(tree.inorder())
# print(tree.bforder())
# print(tree.postorder())
# print(tree.preorder())


# lyst = [1, 2, 3]
# print(lyst)
# # lyst.extend([None])
# # print(lyst)
# lyst.extend([])
# print(lyst)

# sequence0 = [(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
# sequence = []

# print(sequence)

# tree = AVLTree(starting_sequence=sequence)

# print(f"     {tree.root.key}")
# print(f"   /   \\")
# print(f"  {tree.root.left.key}     {tree.root.right.key}")
# print(f" / \\   / \\")
# print(f"{tree.root.left.left.key}   {tree.root.left.right.key} {tree.root.right.left.key}   {tree.root.right.right.key}")










# from tests.car import Car, Color, Make, Model

# def main():
#     print('Hello world!')

#     car = Car(vin='123456789', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
#     print(car)

# if __name__ == '__main__':
#     main()
