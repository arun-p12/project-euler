'''
What is the largest prime factor of the number 600851475143 ?
'''
def p0003_largest_prime_factor(**kwargs):
    n, verbose = 600851475143, 0
    if 'n' in kwargs: num = kwargs['n']
    if 'verbose'in kwargs: verbose = 1

    import time     # get a sense of the time taken
    t = time.time()         # get time just before the main routine

    ########## the main routine #############

    num, primes = n, []     # seed the set of prime #s
    while (num % 2 == 0):  # prime factorize ... keep reducing to account for composites
        num /= 2
        primes.append(2)

    # now that we've handled 2 .... move onto other primes
    next_p = 3
    while next_p <= num:
        while (num % next_p == 0):  # is this a prime number?  [[ composites taken care of below ]]
            num /= next_p           # keep reducing like with 2 above
            primes.append(next_p)
            if(verbose): print(" found : {} and reduced number to {}".format(next_p, int(num)))
        next_p += 2                 # skip even ... odd composites handled above

    ########## end of main routine ###########

    t = time.time() - t             # and now, after the routine
    print("Largest prime factor of {} = {}".format(n, primes[-1]))
    print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t*1000, t*1_000_000))


p0003_largest_prime_factor()
