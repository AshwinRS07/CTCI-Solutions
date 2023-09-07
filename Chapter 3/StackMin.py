# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class stack_min:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val) -> None:
        self.stack.append(val)
        val = min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
    def peek(self) -> int:
        return self.stack[-1]
    def get_min(self) -> int:
        return self.minstack[-1]
    

stack = stack_min()
stack.push(1)
stack.push(2)
stack.push(5)
stack.push(-10)
stack.pop()
min1 = stack.get_min()
print(min1)
print(stack.peek())