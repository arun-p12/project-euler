'''
What is the 10 001st prime number?
'''

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

import sys
sys.path.append('../')
import common as c
number = 10001

primes, mult = [], 10
while(len(primes) < number - 1):
    # not the best logic to generate the right number of primes
    primes = c.prime_list_generator(number*mult, False)
    mult += 10

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("{}st prime = {}".format(number, primes[number - 1]))
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1000000))


