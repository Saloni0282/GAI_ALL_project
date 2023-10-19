class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values == values[::-1]

# Usage: Create a linked list and call is_palindrome(head)
