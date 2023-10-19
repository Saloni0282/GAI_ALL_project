class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class StackUsingLinkedList:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = ListNode(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        item = self.top.val
        self.top = self.top.next
        return item

# Test
stack = StackUsingLinkedList()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1
