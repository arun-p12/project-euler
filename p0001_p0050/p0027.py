'''
for a given quadratic series n^2 + an + b, find the length of the series n that are
consequtively prime. i.e. for all values 0..n the expression resolves to a prime
'''
import sys
sys.path.append('../')
import common as c

# list of consecutive primes for a given a and b
def quad_prime_series(a, b):
    prime = {}
    n = 0
    quad = b
    while(c.is_prime(quad)):
        prime[n] = quad
        n += 1
        quad = (n * n) + (a * n) + b
    return(prime)


# Assist function for quadratic_primes() ... only to handle all combinations of a and b
def max_quad_prime_series(max_len, a, b):
    quad = quad_prime_series(a, b)
    if (len(quad) > max_len):
        max_len = len(quad)
        print("a=", a, "b=", b, "len=", len(quad), "prod=", a * b)
    return(max_len)

'''
When n = 0, n*n + an + b reduces to b. Thus, b must be a prime number.
Following that a must be an odd number, if we consider n = 1, since prime + 1 = composite
'''
def quadratic_primes(number):
    prime = c.prime_list_generator(number, False)

    max_len = 0
    for a in range(3, prime[-1], 2):
        for b in prime:
            max_len = max_quad_prime_series(max_len, a, b)
            max_len = max_quad_prime_series(max_len, a, -b)
            max_len = max_quad_prime_series(max_len, -a, b)
            max_len = max_quad_prime_series(max_len, -a, -b)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

quadratic_primes(1000)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))