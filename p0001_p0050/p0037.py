'''
3797 has an interesting property. Being prime itself, it is possible to continuously
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and
right to left. NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

'''
Correct implementation of truncating number string, from left and right.
1234 returns [1234, 234, 34, 4, 123, 12, 1]

Rather slow, since each number is explicitly checked. 
'''
def truncatable_primes(max, start=23):
    import sys
    sys.path.append('../')
    import common as c
    primes = c.prime_list_generator(max)

    sum, my_list = 0, []
    for i in range(start, max):
        if primes[i]:
            # initialize left with the number,  right with 0, and multiplier of 1
            (left, right, mul, ok) = (i, 0, 1, True)
            while (ok and left > 0):
                right += (left % 10) * mul      # grow the right number
                ok = primes[right] and primes[left]  # check for primeness for early exit
                mul *= 10                       # increase multiplier
                left = int(left / 10)           # shrink the left number
            if ok:                              # is it a truncatable prime?
                sum += i
                my_list.append(i)

    print("sum = ", sum, "len = ", len(my_list), my_list)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

truncatable_primes(1000000)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))