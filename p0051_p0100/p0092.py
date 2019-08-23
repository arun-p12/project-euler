'''
44 → 32 → 13 → 10 → 1 → 1 is formed by taking a number N, and reducing it to the sum of the
squares of its digits. E.g. 44 --> 16 + 16, results in 32. 13 --> 1 + 9, results in 10.
Another sequence is 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89.

How many starting numbers below ten million will arrive at 89?
'''
def square_digit_chain(num=10000000):
    # initialize the chain of numbers seen. Keep them in two separate buckets
    chain = {1: set([1]), 89: set([89])}

    def sum_digit_squares(n):
        return(sum([int(d)**2 for d in str(n)]))

    def is_seen(n):
        # thankfully 0 isn't a key! :)
        for key in chain.keys():
            if(n in chain[key]): return(key)
        return(0)

    def pad_number(n_str, digits=7):
        n_len = len(n_str)
        for i in range(digits - n_len):
            n_str = '0' + n_str
        return(n_str)

    def p92_sdc(num):
        import sys
        sys.path.append('../')
        import common as c

        # num = 10
        for i in range(1, num):

            # if in the set, do nothing.
            if(is_seen(i) == 0):

                # we'll keep updating the next value, append our chain, until it is ok to quit
                next_val, my_chain, ok = i, [i], True
                while(ok):
                    next_val = sum_digit_squares(next_val)
                    my_chain.append(next_val)
                    seen = is_seen(next_val)
                    if(seen):
                        chain[seen].update(set(my_chain))
                        ok = False

                        # while at it, do all permutations of the number
                        pad_i = pad_number(str(i))
                        permu_list = c.permutation_numbers(pad_i)
                        chain[seen].update([int(p) for p in permu_list])
                        #for p in permu_list:
                        #    chain[seen].add(int(p))

                #if((i % 100000) == 0): print ("completed : ", i)

        for key in chain.keys():
            print("len ", key, " = ", len(chain[key]))

    p92_sdc(num)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

square_digit_chain()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1_000_000))
