# Stack of Boxes: You have a stack of n boxes, with widths wi , heights hi, and depths di. The boxes
# cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
# larger than the box above it in width, height, and depth. Implement a method to compute the
# height of the tallest possible stack. The height of a stack is the sum of the heights of each box.

def stack_of_boxes(n, wi, hi, di):
    stack = []
    result = 0

    def backtrack():
        # print(stack)
        nonlocal result
        # if i in stack:
        #     return
        height = 0
        for j in stack:
            height += hi[j]
        print(result, height, stack)
        result = max(result, height)
        if len(stack) == n:
            return
        for j in range(n):
            if j in stack:
                continue
            # if not stack:
            if not stack or (wi[j] < wi[stack[-1]] and hi[j] < hi[stack[-1]] and hi[j] < hi[stack[-1]]):
                stack.append(j)
                backtrack()
                stack.pop()
    backtrack()
    return result

n = 4
wi = [1,2,3,4]
hi = [1,2,3,4]
di = [1,2,3,4]

print(stack_of_boxes(n, wi, hi, di))