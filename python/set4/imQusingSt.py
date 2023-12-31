class QueueUsingStack:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if not self.dequeue_stack:
            return None
        return self.dequeue_stack.pop()

# Test
q = QueueUsingStack()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
q.enqueue(3)
print(q.dequeue())  # Output: 2
print(q.dequeue())  # Output: 3
