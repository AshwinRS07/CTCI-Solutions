# Recursive Multiply: Write a recursive function to multiply two positive integers without using
# the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should
# minimize the number of those operations.

def recursive_multiply(a,b):

    def helper(smaller, bigger):
        if smaller == 0:
            return 0
        elif smaller == 1:
            return bigger
        s = smaller >> 1
        half_prod = helper(s, bigger)

        if (smaller%2==0):
            return half_prod+half_prod
        else:
            return half_prod + half_prod + bigger
        
    
    bigger = a if a>b else b
    smaller = a if a<=b else b
    return helper(smaller, bigger)

tests = [[10,5],[12,50],[31,35],[30,35]]

for a,b in tests:
    print(recursive_multiply(a,b))