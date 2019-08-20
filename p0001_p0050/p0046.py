'''
The smallest odd composite number that cannot be represented as the sum of a prime
and twice a square. E.g. 9 = 7 + 2(1**2) ; 27 = 19 + 2(2**2)

Originally had maintained the list of 2x^2; and then check if for every i, if
the (odd_composite - i) is in that lis. This logic took about 7s to execute.

Modified logic to compute the value of x, and if it is an integer value. [[ from OC = P + 2x^2 ]]
This reduced the execution time to 100ms!!!
'''

def goldbachs_conjecture():
    num = 6000
    primes = ['P'] * num
    primes[0] = primes [1] = primes[2] = 'I'
    for i in range(2, num):
        mult = 2
        while(i * mult < num):
            if(primes[i]): primes[i * mult] = 'C'
            mult += 1

    import math
    odd_comp = [i for i in range(num) if((i % 2) and (primes[i] == 'C'))]
    for oc in odd_comp:
        i, found = 1, False
        while(i < oc):
            root = math.sqrt((oc - i)/2)
            if ((primes[i] == 'P') and (root == int(root))):
                i = oc
                found = True
            i += 2
        if(found == False):
            print("odd composite = ", oc)
            return(0)

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

goldbachs_conjecture()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))