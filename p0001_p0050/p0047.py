'''
N consequtive numbers, of the form A, A+1, A+2, etc... where each of the numbers is the
product of M primes. E.g. 14 = 2x7 and 15 = 3x5. Likewise 644, 645, and 646
'''

def distinct_prime_factors(conseq=3, pf=3):
    import sys
    sys.path.append('../')
    import common as c

    p_factors = c.prime_factors_seive(200000)

    num, cnt = 2, 0
    while (num):  # run forever. we'll exit the instant a match is found
        # keep a counter for the number of consequtive matches found
        # Reset to zero if not a match, and exit when the counter reaches the desired level
        if (len(p_factors[num]) == pf):
            cnt += 1
        else:
            cnt = 0
        if (cnt == conseq):
            print("first num = ", (num - conseq + 1), "last num = ", num)
            return (0)
        num += 1

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

distinct_prime_factors(4, 4)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))

