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

    def print(self): 
        if self.left: 
            self.left.print() 
        print(self.data) 
        if self.right: 
            self.right.print()

    def inorder(self):
        if self.left:
            yield from self.left.inorder()
        yield self.data
        if self.right:
            yield from self.right.inorder()
