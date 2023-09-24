# Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
# find the length of the longest sequence of ls you could create.

def flip_bit_to_win(num):
    if ~num == 0:
        return len(str(bin(num)))
    cur_len = 0
    prev_len = 0
    max_len = 1
    while num!= 0:
        if num&1 == 1:
            cur_len += 1
        elif num&1 == 0:
            prev_len = 0 if num&2 == 0 else cur_len
            cur_len = 0
        max_len = max(max_len, prev_len + cur_len + 1)
        num >>= 1
    return max_len

num = 20
print(flip_bit_to_win(num))