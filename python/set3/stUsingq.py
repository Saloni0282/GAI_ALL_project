from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, val):
        # Push the new element onto queue1
        self.queue1.put(val)

    def pop(self):
        if self.queue1.empty():
            return None

        # Move elements from queue1 to queue2, leaving one element in queue1
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        # Pop the remaining element from queue1 (this is the top of the stack)
        top_element = self.queue1.get()

        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

# Test the stack implementation
stack = StackUsingQueue()
output = []

# Push elements onto the stack
stack.push(1)
stack.push(2)
output.append(stack.pop())  # Pop top element (2)
stack.push(3)
output.append(stack.pop())  # Pop top element (3)
output.append(stack.pop())  # Pop top element (1)

print(", ".join(map(str, output)))  # Output: "2, None, 3, None, None"
