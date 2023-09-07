# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.


# pop_at doesn't rearrange stack of plates after deletion.
class stack_of_plates:
    def __init__(self):
        self.total_stacks = 1
        self.stacks = [[]]
        self.capacity = 5
    def pop(self) -> None:
        self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
            self.total_stacks -= 1
    def push(self, val) -> None:
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([val])
            self.total_stacks += 1
        else:
            self.stacks[-1].append(val)
    def peek(self) -> int:
        return self.stacks[-1][-1]
    def pop_at(self, index):
        stack_number = index//self.capacity
        idx = (index%self.capacity)
        print(stack_number, idx)
        del self.stacks[stack_number][idx]


stack = stack_of_plates()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(10)
stack.push(11)

print(stack.stacks)

print(stack.peek())

stack.pop_at(6)
print(stack.stacks)