'''
Starting from the center, the diagonals are the four corners of a sqaure, and in
crement by 2n.
The center point is a 1x1 square, the next is a 2x2, and so on. Thus, the corners of a 4x4
square would increment by 2x4 = 8, and the diagonals would follow a pattern of
1,    3,5,7,9,    13,17,21,25,       31,37,43,49,     57,65,73,81, ...

'''
def spiral_primes(num=50001):
    import sys
    sys.path.append('../')
    import common as c

    # number of primes found, iteration number, corner values
    cnt, i, adder, corner, ok = 0, 0, 0, 1, True
    while(ok):
        i += 1
        adder += 2              # keeps increasing by 2, 4, 6, 8, ...
        for j in range(4):
            corner += adder
            if (c.is_prime(corner)): cnt += 1        # keep tab of the primes
        prime_ratio = (cnt * 100) / (i * 4 + 1)
        if (prime_ratio < 10):                              # exit condition met?
            print("side = ", 2*i + 1, "[[ ", i, cnt, i * 4 + 1,
                  "{:10.7f}".format((cnt * 100) / (i * 4 + 1)), " ]]")
            ok = False
        #print("side = ", 2*i + 1, " [[ ", i, cnt, i * 4 + 1, "{:10.7f}".format(prime_ratio, " ]]"))


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

spiral_primes()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))