#!/usr/bin/env python3

x1="this is a test"
x2="wokka wokka!!!"
x1_list = [ord(a) for a in x1]
x2_list = [ord(a) for a in x2]
test = list(zip(x1_list,x2_list))
xor = [a[0] ^ a[1] for a in test]
for bit in xor:
    print(bin(bit))

