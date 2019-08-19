'''
28 =  1 + 2 + 4 + 7 + 14 = 28, the sum of its proper divisors. This is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n. 1 + 2 + 3 + 4 + 6 > 12 ; thus 12 is the smallest abundant #

Find the sum of all the positive integers which cannot be written as the sum of two abundant #s.
Note: all integers greater than 28123 can be written as the sum of two abundant numbers.
'''
def non_abundant_sums(number=28123):
    import sys
    sys.path.append('../')
    import common as c

    perf_num = []               # perfect numbers   .... sum of factors = number
    defi_num = []               # deficient numbers .... sum < n  (the num itself isn't counted as factor)
    abun_num = []               # abundant numbers  .... sum > n

    #number = 30
    # classify all numbers as perfect, deficient, or abundant
    # we're only interest in the abundant numbers. but, might as well have the others too.
    for num in range(1, number+1):
        sum_num = sum(c.get_factors(num))
        if(sum_num == 2*num): perf_num.append(num)
        elif(sum_num > 2*num): abun_num.append(num)
        else: defi_num.append(num)
    abundant = set(range(1, number+1))      # save it. We'll discard things that don't apply
    for i in abun_num:
        for j in abun_num:
            if(i + j in abundant): abundant.discard(i+j)

    print("abundant = ", sum(abundant))


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

non_abundant_sums()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))