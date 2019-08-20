'''
125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

# the lead digit must be 1; else 6x will never be a palindrome. 2 x 6 = 12 ... there is an
# extra digit. Also, since x, 2x, 3x, 4x, 5x, 6x are all different numbers, x must have 6-digits
def permuted_multiples():
    # check if two strings have the same digits
    def same_digits(x, y):
        if(sorted(x) == sorted(y)): return(1)
        return(0)

    cnt, ok = 100000, True
    while(ok):
        matched, match_max, ok2 = 0, 6, True
        strings = [str(cnt*i) for i in range(1, match_max + 1)]     # get multiples
        if(sum([same_digits(str(cnt), strings[i]) for i in range(len(strings))]) == match_max):
            print("result = ", cnt, " :: ", cnt*2, cnt*3, cnt*4, cnt*5, cnt*6)
            ok = False          # if check for permutation numbers match, we're done
        cnt += 1

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

permuted_multiples()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))