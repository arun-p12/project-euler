'''
2**6972593 −1 is the first known prime number with over one million digits. Such prime numbers of
the form 2**p - 1 are called Mersenne primes.
What are the last ten digits of  28433(2**7830457)+1 ... a non-Mersenne prime.
'''
def large_non_mersenne_prime(digits=10):
    print("last 10 digits = ", ((28433*(2**7830457 % (10**digits))) + 1) % (10**digits) )

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

large_non_mersenne_prime()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))