'''
sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ...))) Moreover
1 + 1/2 = 3/2; 1 + 1/(2 + 1/2) = 7/5; 1 + 1/(2 + 1/(2 + 1/2)) = 17/12, etc
For the first 1000 expansions, how many fractions contain a numerator with more
digits than the denominator
'''
def square_root_convergents(num=1000):
    from fractions import Fraction

    base, i, match  = Fraction(str(0)), 1, 0
    while(i < num):
        base = 1/(2 + base)
        if(len(str((1 + base).numerator)) > len(str((1 + base).denominator))):
            match += 1
            #print("matches = ", i, 1 + base)
        i += 1
    print("match = ", match)

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

square_root_convergents()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))