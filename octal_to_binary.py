def OctToBin(o):
    return bin(int(o,8))
a=input()
b=OctToBin(a)
print(b[2:])