#!/usr/bin/env python3

s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
sample = [a for a in bytes.fromhex(s)]
keys = list(range(255))

for key in keys:
    xor_list = [ a ^ key for a in sample]
    xor_bytes = bytes(xor_list)
    print("%s(%s): %s" % (key, chr(key), xor_bytes))

