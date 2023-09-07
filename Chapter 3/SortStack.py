# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

class sorted_stack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack1) == 0:
            self.stack1.append(x)
        while len(self.stack1) > 0 and self.stack1[-1] < x:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()
        
    def peek(self) -> int:
        return self.stack1[-1]        

    def empty(self) -> bool:
        if self.stack1:
            return False
        return True

sortedStack = sorted_stack()

sortedStack.push(4)
sortedStack.push(1)
sortedStack.push(8)
sortedStack.push(2)
sortedStack.push(0)
sortedStack.push(9)

print(sortedStack.stack1)