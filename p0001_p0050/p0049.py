'''
A generic routine, that finds a set of three prime numbers, with the interesting property
There are two such sets for 4-digit numbers ... and several more for 5-digit numbers
test
    . 1487, 4817, and 8147 i) contain the same digits, ii) are prime iii) differ by C=3330
'''

# makes no assumption that the difference between the primes is a constant (3330)
def prime_permutations(digits=4):
    import sys
    sys.path.append('../')
    import common as c
    
    max = 10**digits
    primes_bool = c.prime_list_generator(max)
    primes = [x for x in range((10**(digits - 1) - 1), 10**digits) if primes_bool[x]]

    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            next_j = 2 * primes[j] - primes[i]    # C = B + diff ; where diff = B - A
            if(next_j > max): break
            if(primes_bool[next_j]):                         # check for condition #3, (and 2)
                i_list = sorted(str(primes[i]))
                j_list = sorted(str(primes[j]))
                n_list = sorted(str(next_j))

                if((i_list == j_list) and (j_list == n_list)):  # condition #1
                    print("diff = ", "{:7d}".format(primes[j] - primes[i]), " :: ",
                          primes[i], primes[j], next_j)

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

prime_permutations()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
