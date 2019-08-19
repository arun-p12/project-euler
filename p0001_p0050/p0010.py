'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all prime numbers below 2,000,000
'''
import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

import sys
sys.path.append('../')
import common as c

number = 2000000
print("sum of primes = ", sum(c.prime_list_generator(number, False)))

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))
