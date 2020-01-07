#!/usr/bin/env python3

sample = input("Sample string: ")
sample_key = input("Key: ")

def xor_strings(s, key):
    # hex decode to get ASCII Dec value
    sample_bytes = bytes.fromhex(s)
    key_bytes = bytes.fromhex(key)
    # Zip to get tuples and xor them
    xor_list = [a ^ b for a,b in zip(sample_bytes,key_bytes)]
    # Convert list to bytes
    xor_bytes = bytes(xor_list)
    #print(s1_bytes)
    #print(s2_bytes)
    #print(xor_list)
    #print(xor_bytes)
    # Hex result to compare with expected value
    xor_result = bytes.hex(xor_bytes)

    print(xor_result)
    return xor_result


cypher_text = xor_strings(sample,sample_key)

#TEST
if xor_strings(cypher_text,sample_key) == sample:
    print("SUCCESS!!!")
else:
    print("FAIL")
