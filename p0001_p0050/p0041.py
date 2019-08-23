'''
What is the largest pandigital prime number?

1+2+3+4+5+6+7+8 = 36, which is divisible by 3. Thus, all 8-digit pandigital numbers are
composite. By extension all 9-digit pandigital numbers are also composite. Thus, the largest
pandigital number must be 7-digit
'''
def largest_pandigital_prime(num):
    import sys
    sys.path.append('../')
    import common as c
    pand_list = c.permutation_numbers(str(num))

    for item in pand_list:
        int_item = int(item)
        if((int_item % 2) and (int_item % 5)):
            if(c.is_prime(int_item)): break
    print("max = ", int_item)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

largest_pandigital_prime(7654321)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
