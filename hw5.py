# from datastructures.intervaltree import IntervalNode, IntervalTree

# test = IntervalNode(low=1)

# print(test.height)
# print(test.intervals_at_low)

from datastructures.intervaltree import IntervalTree

tree = IntervalTree()

tree.interval_insert(high=5, low=2, data=[5, 2, "2-5", ":)"])
tree.interval_insert(high=8, low=2, data=[8, 2, "2-8", ":D"])
tree.interval_insert(high=9, low=5, data=[9, 5, "5-9", ":P"])
tree.interval_insert(high=2, low=1, data=[2, 1, "1-2", ":O"])
tree.interval_insert(high=10, low=1, data=[10, 1, "1-10", ":|"])

print(tree.search(point=3)) # should have 5, 8, 10
print(tree.search(point=8)) # should have 8, 9, 10
print(tree.search(point=9)) # should have 9, 10
print(tree.inorder())