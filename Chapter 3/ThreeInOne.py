# Three in One: Describe how you could use a single array to implement three stacks.

# Divide array in 3 parts for each to serve as a stack.

# Initial nums values are not considered, might be better to just specify length in constructor parameters and create the nums array in the constructor
# Note that the solution is not thoroughly tested yet. Feel free to contribute edge case testing!
class create_stacks:
    def __init__(self, nums):
        if len(nums)<3: return False
        self.nums = nums
        self.n = len(nums)
        self.topA, self.topB, self.topC = 0, self.n//3-1, 2*(self.n//3)-1
    def push(self,stack: int, val: int):
        if stack == 0:
            if self.topA == self.n//3-2:
                return False
            else:
                self.topA += 1
                self.nums[self.topA] = val
        if stack == 1:
            if self.topB == (2*self.n//3)-2:
                return False
            else:
                self.topB += 1
                self.nums[self.topB] = val
        if stack == 2:
            if self.topC == self.n-1:
                return False
            else:
                self.topC += 1
                self.nums[self.topC] = val
        return True
    def pop(self, stack: int):
        if stack == 0:
            if self.topA == -1:
                return -1
            else:
                val = self.nums[self.topA]
                self.topA -= 1
                return val
        if stack == 0:
            if self.topB == self.n//3-2:
                return -1
            else:
                val = self.nums[self.topB]
                self.topB -= 1
                return val
        if stack == 0:
            if self.topC == (2*self.n//3)-2:
                return -1
            else:
                val = self.nums[self.topC]
                self.topC -= 1
                return val
    def peek(self,stack):
        if stack == 0:
            return self.nums[self.topA] if self.topA != -1 else -1
        elif stack == 1:
            return self.nums[self.topB] if self.topB != self.n//3-2 else -1
        elif stack == 2:
            return self.nums[self.topC] if self.topC != (2*self.n//3)-2 else -1
        
nums = [0]*9
stax = create_stacks(nums)
print("topA:",stax.peek(0),"   topB:",stax.peek(1),"  topC:",stax.peek(2))
stax.pop(0)
print("topA:",stax.peek(0),"   topB:",stax.peek(1),"  topC:",stax.peek(2))
stax.push(1,10)
print("topA:",stax.peek(0),"   topB:",stax.peek(1),"  topC:",stax.peek(2))
stax.push(0,20)
print("topA:",stax.peek(0),"   topB:",stax.peek(1),"  topC:",stax.peek(2))
print(stax.nums)