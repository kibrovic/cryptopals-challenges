#!/usr/bin/env python3

#string = """Burning 'em, if you ain't quick and nimble
#I go crazy when I hear a cymbal"""
#
#key = "ICE"
#
#xor_list = [ord(a) ^ ord(key[i%len(key)]) for i, a in enumerate(string)]
#
#xor_cipher = bytes.hex(bytes(xor_list))
#
#match = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
#a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""
#
#match.strip()

#if xor_cipher == "".join(match.split('\n')):
#    print("Success", xor_cipher)
#else:
#    print("FAIL")

def repeating_xor(s,k):
    xor_list = xor_list = [ord(a) ^ ord(k[i%len(k)]) for i, a in enumerate(s)]
    xor_cipher = bytes.hex(bytes(xor_list))
    #print(xor_cipher)
    return xor_cipher

def main():
    string = """Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"""
    key = "ICE"
    #match = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
    #a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""
    match = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""
    if repeating_xor(string,key) == match:
        print("Success")
    else:
        print("FAIL")

if __name__ == '__main__':
    main()
