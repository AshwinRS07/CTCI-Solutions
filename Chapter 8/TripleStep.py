# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.

def triple_step_iter(n: int) -> int:
    if n == 0:
        return 1
    elif n <= 2:
        return n
    i,j,k = 0,1,2
    for step in range(3,n+1):
        # cur = i+j+k
        i,j,k = j,k,i+j+k
    return k

def triple_step_recurse(n: int, memo: list) -> int:
    if n in memo:
        return memo[n]
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        memo[n] = triple_step_recurse(n-1, memo) + triple_step_recurse(n-2, memo) + triple_step_recurse(n-3, memo)
        return memo[n]

tests = [1,2,3,4,5,6,7,8,9,10]

for test in tests:
    print(triple_step_recurse(test, {}))