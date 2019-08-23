'''
7**5 = 16,807 (A 5-digit number). 8**9 = 134,217,728 (a 9-digit number)
How many n-digit positive integers exist which are also an nth power?
'''
def powerful_digit_counts():
    max_power, result = 25, 0
    for i in range(1, max_power):
        cnt, ok = 1, True
        while(ok):
            val = cnt**i
            val_len = len(str(val))
            if(val_len == i):
                result += 1
                print("result = ", result, " :: ", cnt, i, val)
            else:
                if(val_len >= i): ok = False
            cnt += 1

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

powerful_digit_counts()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1_000_000))
