'''
Numbers that are triangular [ n(n+1)/2 ], pentagonal [ n(3n -1/2 ], and hexagonal [ n(2n -1) ]

rather than creating three lists, and comparing if an element is in each of them, we can reduce
the problem space by:
    - ignoring the triangular list, since every element in it, will also be in the hex list
    - take the hex_list, and solve for P using the pent_list (could do the reverse too)
            . P = (3n^2 - n) / 2 =>  3n^2 -n -2P = 0 ; now solve for integer value of n
'''
def tri_pent_hex(num):
    tri_list = [(n*(n + 1) / 2) for n in range(num)]
    pent_list = [(n*(3*n - 1) / 2) for n in range(num)]
    hex_list = [(n*(2*n - 1)) for n in range(num)]

    import math
    for x in hex_list:
        #if((x in pent_list) and (x in hex_list)): print(x)
        #if (x in pent_list): print(x)
        root = (1 + math.sqrt(1 + 24*x))/6
        if(root == int(root)): print("ans = ", x)

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

tri_pent_hex(100000)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))