'''
If the add the alphabetical position of SKY we get 55 (assuming A=1, and Z=26).
55 is a triangle number, because it can be represented by n(n+1)/2.

In a given list of words, how many are triangular?
'''
def coded_triangle_numbers():
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    triangle_sum = [int(i*(i+1)/2) for i in range(100)]   ## not more than a 100-letter word!! :)

    for line in open('p0042_words.txt', "r").readlines():
        # remove all double-quotes, strip out newline, split out the words, save into a list
        words = line.replace('"', '').strip().split(',')

    result, discard = {}, {}
    for my_word in words:
        w_sum = 0
        for letter in my_word:
            w_sum += alphabets.index(letter) + 1
        if(w_sum in triangle_sum): result[my_word] = w_sum
        else: discard[my_word] = w_sum
    print("len = ", len(result))
    #print(result, discard)

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

coded_triangle_numbers()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
