# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.


#Basically, we keep the stack reversed so it acts as a queue.
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(x)
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
