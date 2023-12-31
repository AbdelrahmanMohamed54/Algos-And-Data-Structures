# flattened tree function:
# 12.3


def flatten(tree):
    for node in tree:
        if isinstance(node, list):
            yield from flatten(node)
        else:
            yield node


tree = [[1], [2, 3], [4, [5, 6, [7, 8, [9, [10, 11, 12]]]]]]
flattened_tree = list(flatten(tree))
print(flattened_tree)
