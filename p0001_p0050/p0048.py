'''
Find the least-N significant digits of a series of numbers, raised to itself.
test :: 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317
'''

# use modulo division to get the least significant digits.
def self_powers(num, digits=10):
    last_dig = 0
    for i in range(1, num+1):
        last_dig = ((last_dig + (i**i) % (10**digits)) % (10**digits))
    print("last digits = ", last_dig)

    # sum([i**i for i in range(1,1001)]) % 10000000000      # sngle liner


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

self_powers(1000)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
