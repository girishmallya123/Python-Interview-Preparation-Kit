'''
class that represents the stack
'''
class Stack():
    def __init__(self):
        self.data = []

    # Push a value to the stack
    def push(self, val):
        self.data.append(val)

    # Remove the last element from stack
    def pop(self):
        self.data.pop()

    # Check if the stack is empty
    def is_empty(self):
        return len(self.data) == 0

    # Get the top element of the stack
    def peek(self):
        if not self.is_empty():
            return self.data[-1]

def main():
    print("Stack examples!")
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.pop()

if __name__ == "__main__":
    main()
