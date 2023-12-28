# R-6.1

"""
push(5): Stack: [5]
push(3): Stack: [5, 3]
pop(): Returns 3. Stack: [5]
push(2): Stack: [5, 2]
push(8): Stack: [5, 2, 8]
pop(): Returns 8. Stack: [5, 2]
pop(): Returns 2. Stack: [5]
push(9): Stack: [5, 9]
push(1): Stack: [5, 9, 1]
pop(): Returns 1. Stack: [5, 9]
push(7): Stack: [5, 9, 7]
push(6): Stack: [5, 9, 7, 6]
pop(): Returns 6. Stack: [5, 9, 7]
pop(): Returns 7. Stack: [5, 9]
push(4): Stack: [5, 9, 4]
pop(): Returns 4. Stack: [5, 9]
pop(): Returns 9. Stack: [5]
"""

# R-6.10

"""
If the loop in the ArrayQueue.resize method were implemented as self.data[k] = old[k] instead of
self.data[k] = old[walk], it would cause incorrect elements to be copied during the resizing process.
This would lead to the loss of elements and incorrect repositioning of elements within the underlying array.

Here's a detailed explanation of what could go wrong:

The ArrayQueue.resize method is responsible for resizing the underlying array to accommodate more elements if needed.

The original implementation uses a variable walk to keep track of the position within the existing array old from which
elements should be copied.

However, if the loop were changed to self.data[k] = old[k], it would disregard the intended circular shifting of indices
and directly copy elements based on the indices of old.

This would cause elements to be copied from old to self.data in a sequential manner, without considering the circular
nature of the queue.

As a result, the elements in the resized array self.data would not align correctly with the front of the queue.

Additionally, if the front of the queue is not at the beginning of old, the copied elements would not be positioned
correctly within self.data.

Subsequent operations on the queue, such as enqueueing or dequeuing elements, would lead to incorrect behavior and
possibly result in errors or data loss.

Therefore, using self.data[k] = old[k] instead of self.data[k] = old[walk] in the resizing loop would break the intended
circular shifting of indices and result in incorrect element placement and potential data loss within the resized array.

"""

# R-6.12 (page 247 in the book has good info on this question)

"""
add first(4): Deque: [4]
add last(8): Deque: [4, 8]
add last(9): Deque: [4, 8, 9]
add first(5): Deque: [5, 4, 8, 9]
back(): Returns 9
delete first(): Returns 5. Deque: [4, 8, 9]
delete last(): Returns 9. Deque: [4, 8]
add last(7): Deque: [4, 8, 7]
first(): Returns 4
last(): Returns 7
add last(6): Deque: [4, 8, 7, 6]
delete first(): Returns 4. Deque: [8, 7, 6]
delete first(): Returns 8. Deque: [7, 6]
"""

# C-6.17