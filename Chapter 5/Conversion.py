# Conversion: Write a function to determine the number of bits you would need to flip to convert
# integer A to integer B.

def conversion(a,b):
    print(bin(a),bin(b))
    count = 0
    c = a^b
    while c!=0:
        c = c >> 1
        count += (c&1)
    return count

a,b = 13,7

print(conversion(a,b))