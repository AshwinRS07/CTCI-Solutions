# Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
# the binary representation. If the number cannot be represented accurately in binary with at most 32
# characters, print "ERROR:'

def binary_to_string(num):
    if num >=1 or num <=0:
        print('1')
        return 'ERROR'
    binary = '.'
    while num > 0:
        if len(binary) >= 32:
            print('2')
            return 'ERROR'
        res = num * 2
        if res >= 1:
            binary += '1'
            num = res-1
        else:
            binary += '0'
            num = res
        print(binary)
    return binary

num = 0.0625

print(binary_to_string(num))