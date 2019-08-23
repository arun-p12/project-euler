'''
Did a bit of manual work... rather than do everything programmatically.
Using the various keys, wrote the decoded message to a file. Then searched for common words
such as 'the' ... found a key that had the maximum occurances of it, and confirmed that
other words decoded were also regular english words.
'''
def xor_encryption(file='./p0059_cipher.txt'):
    # brute force.... create a list of all possible combinations of keys
    def gen_key(k_len=3):
        base = 'abcdefghijklmnopqrstuvwxyz'
        key = []
        for k1 in base:
            for k2 in base:
                for k3 in base:
                    key.append(ord(k1))
                    key.append(ord(k2))
                    key.append(ord(k3))
        return(key)

    def extend_key(key, msg_len):
        k_len = len(key)
        quo = msg_len // k_len
        rem = msg_len % k_len
        key *= quo
        for i in range(rem):
            key.append(key[i])
        return(key)

    # read the encoded file, and generate the full key list
    enc_list = [int(x) for x in open(file, "r").readline().split(',')]
    key_list = gen_key()

    key = []
    for i in range(0, len(key_list), 3):
        key = key_list[i:i+3:]
        #print("iteration : ", i/3, [chr(i) for i in key])
        key = extend_key(key, len(enc_list))
        decode_list = [chr(enc_list[i] ^ key[i]) for i in range(len(key))]
        #print(decode_list)
        if(i/3 == 3317):            # looked for 't', 'h', 'e' and got key='exp'
            print("result = ", sum([ord(decode_list[i]) for i in range(len(decode_list))]))
            break


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

xor_encryption()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1_000_000))
