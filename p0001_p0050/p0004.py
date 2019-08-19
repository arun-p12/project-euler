'''
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time  # get a sense of the time taken

t = time.time()  # get time just before the main routine

########## the main routine #############

maxp, ii, jj = 0, 0, 0
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        p = i * j
        if str(p) == str(p)[::-1] and p > maxp: ii, jj, maxp = i, j, p


########## end of main routine ###########

t = time.time() - t             # and now, after the routine
print("Required palindrome is {} :: product of {} and {}".format(maxp, ii, jj))
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t*1000, t*100000))
