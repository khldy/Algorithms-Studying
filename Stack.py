class Stack:
    def __init__(self):
        self.stack = []

    # Push (Add to the rop)
    def push(self, item):
        self.stack.append(item)

    # Pop (Remove from the top)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    #Get the size of the stack
    def size(self):
        return len(self.stack)

#Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print('Stack: ', stack.stack)

print('Pop: ', stack.pop())
print('Stack after pop: ', stack.stack)

print('Top element: ', stack.peek())