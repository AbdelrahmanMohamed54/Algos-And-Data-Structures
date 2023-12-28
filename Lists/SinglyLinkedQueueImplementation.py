# Implement a queue using a singly linked list.
# The solution is on page 264 in the goodrich book

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:

        """Lightweight, nonpublic class for storing a singly linked node."""

        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node’s fields
            self._element = element  # reference to user’s element
            self._next = next  # reference to next node

    def __init__(self):
        """ Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0  # number of queue elements

    def len(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element  # front aligned with head of list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """

        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # special case as queue is empty
            self._tail = None  # removed head had been the tail
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)  # node will be new tail node
        if self.is_empty():
            self._head = newest  # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest  # update reference to tail node
        self._size += 1


class Empty(Exception):
    pass


"""
To implement a queue using the provided implementation of the singly linked list (LinkedStack), you can utilize the 
concept of a doubly ended queue (deque). The deque allows insertion and removal of elements at both ends, which 
corresponds to the enqueue and dequeue operations in a queue.

In the above implementation, the enqueue operation corresponds to pushing elements onto the LinkedStack, and the dequeue 
operation involves temporarily reversing the order of elements to access and remove the frontmost element. The front 
method retrieves the frontmost element without removing it. The LinkedQueue class provides a queue interface while 
internally using the LinkedStack implementation.
"""

# Create an instance of LinkedQueue
queue = LinkedQueue()

# Test is_empty() on an empty queue
print(queue.is_empty())  # Output: True

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Test is_empty() on a non-empty queue
print(queue.is_empty())  # Output: False

# Test len() method
print(queue.len())  # Output: 3

# Test first() method
print(queue.first())  # Output: 1

# Dequeue elements
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

# Test len() method after deque
print(queue.len())  # Output: 1

# Enqueue another element
queue.enqueue(4)

# Test first() method after enqueue
print(queue.first())  # Output: 3

# Dequeue the remaining element
print(queue.dequeue())  # Output: 3

# Test is_empty() on an empty queue after dequeuing all elements
print(queue.is_empty())  # Output: True
