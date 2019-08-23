'''
find the prime #, that is a sum of N consequtive primes; where N is maximized.
test
    . 2 + 3 + 5 + 7 + 11 + 13 = 41          (largest sequence where sum is less than 100)
    . 7 + 11 + 13 + ... (21 items) = 953    (largest sequence where sum is less than 1000)
'''
def consequtive_prime_sum(max=100):
    import sys
    sys.path.append('../')
    import common as c

    primes_bool = c.prime_list_generator(max)   # [False, False, True, True, False, ...]
    primes = c.prime_list_generator(max, False) # [2, 3, 5, 7, 11, ...]

    start, len_max, max_sum = 0, 0, 0       # where the results are stored
    for i in range(len(primes)):
        sum = primes[i]                     # initialize sum
        for j in range(i+1, len(primes)):
            sum += primes[j]
            if(sum < max):                  # if sum is out of range, skip the larger primes
                if(primes_bool[sum]):       # if 2nd conditional also met...
                    l = j - i + 1           # calculate length of the series
                    if(l > len_max): len_max, start, max_sum = l, primes[i], sum
            else: break
    print("start = ", start, " :: ", "max = ", len_max, " :: ", "sum = ", max_sum)

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

consequtive_prime_sum(1_000_000)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
