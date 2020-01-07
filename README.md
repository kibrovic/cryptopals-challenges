### S1C1: Convert hex to base64

**Cryptopals Rule:**

> Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

```
echo "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d" | xxd -r -p | base64
```

### S1C2: Fixed XOR

`fixed-xor.py` file

If sample text contains string values, they can't be XOR-ed. Hex decoding given string (and key just in case) will return [ASCII Dec value](https://donsnotes.com/tech/charsets/ascii.html). These can be XOR-ed. Result needs to be hex encoded again. 

XOR on resulting text with same key needs to return the sample text

### S1C3: Single-byte

`signle-byte-xor.py' file

Brute force sample with English Alphabet letters and find the most logical result. This should be done using probability and one day it might.

### S1C4: Detect single-character XOR

Brute force using probability. Characters frequency taken from [Practical Cryptography](http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/#monogram-frequencies). Result with highest probability is taken as most likely result

### S1C5: Implement repeating-key XOR

Key is handling which key character shoudld be used for XOR. Using Modulus operator (%) helps. Dividing string char's position with lenght of XOR key will return remainder which is always smaler than key length and increments by one. Using this result as position for key solves the problem. Example:

```
>>> key = "ICE"
>>> len(key)
3
>>> 0%3
0
>>> 1%3
1
>>> 2%3
2
>>> 3%3
0
>>> 4%3
1
```



