# Extended Tree Implementation
# 12.1


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.data)
        if self.right:
            self.right.print_inorder()

    def inorder(self):
        if self.left:
            yield from self.left.inorder()
        yield self.data
        if self.right:
            yield from self.right.inorder()

    def print_preorder(self):
        print(self.data)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def preorder(self):
        yield self.data
        if self.left:
            yield from self.left.preorder()
        if self.right:
            yield from self.right.preorder()

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.data)

    def postorder(self):
        if self.left:
            yield from self.left.postorder()
        if self.right:
            yield from self.right.postorder()
        yield self.data


# Testing the tree:
"""
# Create a binary tree
root = Node(4)
root.insert(2)
root.insert(6)
root.insert(1)
root.insert(3)
root.insert(5)
root.insert(7)

# Print in-order traversal
print("In-order Traversal:")
root.print_inorder()

# Generator-based in-order traversal
print("\nIn-order Traversal (Generator):")
for value in root.inorder():
    print(value)

# Print pre-order traversal
print("\nPre-order Traversal:")
root.print_preorder()

# Generator-based pre-order traversal
print("\nPre-order Traversal (Generator):")
for value in root.preorder():
    print(value)

# Print post-order traversal
print("\nPost-order Traversal:")
root.print_postorder()

# Generator-based post-order traversal
print("\nPost-order Traversal (Generator):")
for value in root.postorder():
    print(value)

"""