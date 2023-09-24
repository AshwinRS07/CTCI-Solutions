# Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
# j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
# can assume that the bits j through i have enough space to fit all of M. That is, if
# M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
# example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.

# Mask should be all 1's except for i to j
# Left 1's Mask = (-1 << (j+1))
# Right 1's Mask = (1<<j)-1


def insertion(m: bin, n: bin, i, j):
    lefts = (~0 << (j+1))
    rights = ((1<<i)-1)
    print("lefts:",bin(lefts)," rights:",bin(rights))
    mask = lefts | rights
    print(bin(mask))
    cleared = n & mask
    # print(bin(cleared))
    moved = m << i
    return cleared | moved

m = int("10011",2)
n = int("10000000000",2)
i = 2
j = 6


# m,n,i,j = int("11111111111", 2), int("10011", 2), 2, 6
print(bin(insertion(m,n,i,j)))  