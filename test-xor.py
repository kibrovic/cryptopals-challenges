#!/usr/bin/env python3

with open('6.txt', 'r') as file:
    encrypted_text = file.read().replace('\n', '')

print(encrypted_text)

# Humming distance function
def humming_distance(string1,string2):
    string1_list=[ord(a) for a in string1]
    string2_list=[ord(a) for a in string2]
    xor_list=[a[0] ^ a[1] for a in list(zip(string1_list,string2_list))]
    count=[int(a) for bit in xor_list for a in bin(bit) if a=='1']
    return sum(count)

# KEYSIZE list
keys=list(range(2,41))

# TEST humming_distance function
x1="this is a test"
x2="wokka wokka!!!"
test=humming_distance(x1,x2)
if test != 37:
    print('FAIL ', test)
else:
    print("All good!!! ", test)

probability = [{"key":key, "distance":humming_distance(encrypted_text[:key],encrypted_text[key:key*2])/key} for key in keys]
probability_sorted = sorted(probability, key=lambda x: x["distance"])
print(probability_sorted)

blocks = [encrypted_text[i:i+7] for i in range(0,len(encrypted_text),7)]

transposed_blocks=[]
for i in range(0,7):
    bits=[block[i] for block in blocks]
    transposed_blocks.append("".join(bits))

print(transposed_blocks)
