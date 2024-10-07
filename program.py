from datastructures.avltree import AVLTree, AVLNode
import random
# from collections import deque

from tests.car import Car, Color, Make, Model

def main():

    tree = AVLTree()

    for node in [8, 9, 10, 2, 1, 5, 3, 6, 4, 7]:
            tree.insert(key=node, value=node)

    #printing all traversals of tree
    print(f"{'inorder:':10} {tree.inorder()}")
    print(f"{'bforder:':10} {tree.bforder()}")
    print(f"{'preorder:':10} {tree.preorder()}")
    print(f"{'postorder:':10} {tree.postorder()}")

    #check that they are correct
    assert tree.inorder() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert tree.bforder() == [5, 3, 8, 2, 4, 6, 9, 1, 7, 10]
    assert tree.preorder() == [5, 3, 2, 1, 4, 8, 6, 7, 9, 10]
    assert tree.postorder() == [1, 2, 4, 3, 7, 6, 10, 9, 8, 5]

    tree.delete(key=7)
    #check that they are still correct after deleting 7
    assert tree.inorder() == [1, 2, 3, 4, 5, 6, 8, 9, 10]
    assert tree.bforder() == [5, 3, 8, 2, 4, 6, 9, 1, 10]
    assert tree.preorder() == [5, 3, 2, 1, 4, 8, 6, 9, 10]
    assert tree.postorder() == [1, 2, 4, 3, 6, 10, 9, 8, 5]

    tree.insert(key=7, value=7)
    tree.delete(key=8)
    # check that they are still correct after deleting 8
    assert tree.inorder() == [1, 2, 3, 4, 5, 6, 7, 9, 10]
    assert tree.bforder() == [5, 3, 9, 2, 4, 6, 10, 1, 7]
    assert tree.preorder() == [5, 3, 2, 1, 4, 9, 6, 7, 10]
    assert tree.postorder() == [1, 2, 4, 3, 7, 6, 10, 9, 5]

    tree.insert(key=8, value=8)
    tree.delete(key=5)
    tree.delete(key=6)
    tree.delete(key=7)
    tree.delete(key=8)
    tree.delete(key=9)
    # check that they are still correct after deleting 5-9
    print(f"{'inorder:':10} {tree.inorder()}")
    print(f"{'bforder:':10} {tree.bforder()}")
    print(f"{'preorder:':10} {tree.preorder()}")
    print(f"{'postorder:':10} {tree.postorder()}")

    print("it worked :D")

if __name__ == '__main__':
    main()

