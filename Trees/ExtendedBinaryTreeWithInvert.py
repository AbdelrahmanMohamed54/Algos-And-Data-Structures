# Extended Tree Implementation with invert function added
# 12.2


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

    def invert(self):
        if self is None:
            return None

        # Recursively invert the left and right subtrees
        inverted_left = self.left.invert() if self.left else None
        inverted_right = self.right.invert() if self.right else None

        # Swap the left and right subtrees
        self.left = inverted_right
        self.right = inverted_left

        return self



# Create a binary tree
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)

# Invert the binary tree using the invert method
root.invert()

# Print the inverted binary tree
root.print_inorder()
