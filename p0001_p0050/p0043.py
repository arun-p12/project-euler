'''
In 1406357289 (a 0 to 9 pandigital number), 406 (digits 2, 3, and 4) is divisible by 2.
063 (digits 3, 4, and 5) is divisible by 3, 635 (digits 4, 5, 6) is divisible by 5, etc.
The last set, 289 (digits 8, 9, and 10) is divisible by 17.

To find the sum of all 0-9 pandigital numbers with this property.
'''
def substring_divisibility():
    import sys
    sys.path.append('../')
    import common as c

    pand_list = c.permutation_numbers('9876543210')
    #pand_list = ['1406357289']
    primes = ['', 2, 3, 5, 7, 11, 13, 17]

    (sum, result) = (0, [])
    for p in pand_list:
        (i, ok) = (1, True)
        while(ok and (i < 8)):
            # pick the 3-digit substring
            if(int(p[i:i+3:]) % primes[i]): ok = False
            i += 1
        if(ok):
            result.append(p)
            sum += int(p)
    print("sum = ", sum, result)

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

substring_divisibility()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))