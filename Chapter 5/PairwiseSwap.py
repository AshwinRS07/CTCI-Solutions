# Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
# possible (e.g., bit O and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

def pairwise_swap(number):
    mask_10 = 0xAAAAAAA
    mask_01 = 0x5555555
    num_even = number & mask_10
    num_odd = number & mask_01
    swap_num = (num_even>>1) | (num_odd<<1)
    print(bin(swap_num))
    return swap_num


number = 22
print(bin(number))
print(pairwise_swap(number))