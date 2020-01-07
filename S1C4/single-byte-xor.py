#!/usr/bin/env python3

with open("4.txt", "r") as f:
    s = [line.strip() for line in f]

# Courtesy of practical cryptography
# http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/
frequencies = {
        "A": 8.55, "B": 1.60, "C": 3.16, "D": 3.87, "E": 12.10, "F": 2.18, "G": 2.09, "H": 4.96, "I": 7.33, "J": 0.22, "K": 0.81, "L": 4.21, "M": 2.53, "N": 7.17, "O": 7.47, "P": 2.07, "Q": 0.10, "R": 6.33, "S": 6.73, "T": 8.94, "V": 1.06, "W": 1.83, "X": 0.19, "Y": 1.72, "Z": 0.11
        }

samples = [bytes.fromhex(a) for a in s]
keys = list(range(0,255))

scores = []

for sample in samples:
    for key in keys:
        xor_list = [a ^ key for a in sample]
        xor_bytes = bytes(xor_list)
        score = sum([frequencies.get(chr(freq),0) for freq in xor_bytes.upper()])
        scores.append({"message": xor_bytes, "key": key, "score": score})

scores = sorted(scores, key=lambda score: score["score"])
match = scores[len(scores)-1]
print("Best match:", match)
