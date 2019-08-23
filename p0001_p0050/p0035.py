'''
197 is circular prime because 197, 971, and 791 are all primes...
These numbers are formed by rotating the sequence of the digits
'''

'''
Given a number 123 .... return 123, 231, and 312..... the circular list
But, not 132, 213, and 321
'''
def circ_numbers(string):
    ret_list = []
    my_len = len(string)
    for i in range(my_len):
        my_str = string[i]
        for j in range(1, my_len):
            new_loc = ((i + j) % my_len)        # do the wrap around
            my_str += string[new_loc]
        ret_list.append(my_str)
    return(ret_list)

'''
reduce the set by eliminating obvious candidates.If the number contains a 5, 
or an even number; then one of the circular numbers will be a composite. Ignore those
'''
def can_be_circular_prime(n):
    for x in str(n):
        xi = int(x)
        if((xi % 2) == 0): return(False)        # has an even digit
        if(xi == 5): return(False)              # has a '5'
    return(True)

def circular_primes(number, start=0):

    #number = 100
    primes = c.prime_list_generator(number)

    # cycle thru the prime numbers, and save the circular primes.
    circ_prime = {}
    for i in range(len(primes)):
        if(primes[i]):
            circ_list = circ_numbers(str(i))      # get circular list of numbers
            cnt, len_circ, ok = 0, len(circ_list), True
            while(ok and (cnt < len_circ)):
                if(primes[int(circ_list[cnt])] == False): ok = False
                else: cnt +=1
            if(cnt == len_circ): circ_prime[i] = 1      # circular list is prime

    print("len = ", len(circ_prime), " :: ", sorted(circ_prime.keys()))

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############
import sys
sys.path.append('../')
import common as c
circular_primes(1_000_000)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
