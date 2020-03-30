#!/usr/bin/env python3

import base64

with open('6.txt', 'r') as file:
    encrypted_text = base64.b64decode(file.read().replace('\n', ''))


# Humming distance function
def humming_distance(string1,string2):
    xor_list=[a[0] ^ a[1] for a in list(zip(string1,string2))]
    count=[int(a) for bit in xor_list for a in bin(bit) if a=='1']
    return sum(count)


# TEST humming_distance function
#if humming_distance(bytes("this is a test","utf-8"), bytes("wokka wokka!!!","utf-8")) != 37:
#    print('FAIL')
#else:
#    print('ALL GOOD!!!')

# For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
def calculate_probability(s):
    probability =[]
    for keysize in range(2,41):
        # Split text in chunks of keysize length
        chunks = [s[i:i+keysize] for i in range(0,len(s),keysize)]
        # Calculate distances
        distances =[]
        for i in range(0,len(chunks),2):
            try:
                distances.append(humming_distance(chunks[i],chunks[i+1])/keysize)
            except IndexError:
               break
        # normalize distances
        average_distance = sum(distances)/len(distances)
        probability.append({
            "keysize": keysize,
            "distance": average_distance
            })
    # The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values.
    probability_sorted = sorted(probability, key=lambda x: x["distance"])
    print(probability_sorted[0])
    return probability_sorted[0]['keysize']

def transpose_blocks(s,k):
    blocks = [s[i:i+k] for i in range(0,len(s),k)]
    transposed_blocks=[]
    for i in range(0,len(blocks[0])):
        tmp = []
        for j in range(0,len(blocks)):
            try:
               tmp.append(blocks[j][i])
            except IndexError:
               break
        transposed_blocks.append(tmp)
    return transposed_blocks

def single_byte_xor(s):
    # based on english letter frequencies from wikipedia, space estimated
    # https://en.wikipedia.org/wiki/Letter_frequency
    frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    #samples = [bytes.fromhex(a) for a in s]
    keys = list(range(0,255))
    scores = []
    #for sample in s:
    for key in keys:
        xor_list = [a ^ key for a in s]
        xor_bytes = bytes(xor_list)
        score = sum([frequencies.get(chr(freq),0) for freq in xor_bytes.upper()])
        scores.append({"message": xor_bytes, "key": key, "score": score})
    scores = sorted(scores, key=lambda score: score["score"])
    match = scores[len(scores)-1]
    print("Best match:", match)
    return match['key']

def repeating_xor(s,k):
    xor_list = xor_list = [a ^ k[i%len(k)] for i, a in enumerate(s)]
    return bytes(xor_list)

def main():
    with open('6.txt', 'r') as file:
        encrypted_text = base64.b64decode(file.read().replace('\n', ''))
    likeliest_keysize = calculate_probability(encrypted_text)
    transposed_blocks = transpose_blocks(encrypted_text, likeliest_keysize)
    repeating_key = [single_byte_xor(block) for block in transposed_blocks]
    message = bytes(repeating_xor(encrypted_text,repeating_key))
    print('\n\n')
    print('Key: ', bytes(repeating_key))
    print('Message: ', message)


if __name__ == '__main__':
    main()
