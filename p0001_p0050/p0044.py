'''
pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
E.g. in 1, 5, 12, 22, 35, 51, 70, 92, 117, 145 ... 22 + 70 = 92 which is pentagonal
      but, 70 - 22 = 52 isn't
'''
def pentagon_numbers():
    pent_list = [(n*(3*n - 1) / 2) for n in range(1, 2500)]
    pent_set = set()

    # do the reverse... assume add and sub are pentagonal.
    # validate if there exists a p1 and p2 to assert the assumption.
    for p_add in pent_list:
        pent_set.add(p_add)
        for p_sub in [x for x in pent_set if x < p_add]:    # this would be the smaller vals
            p2 = 0.5 * (p_add + p_sub)                      # compute Pn2
            if p2 in pent_set:
                p1 = p_add - p2                             # compute Pn1
                if p1 in pent_set:                          # Wow!
                    print("diff = ", int(p2 - p1), " :: ", "index = ",
                          pent_list.index(p2), pent_list.index(p1),
                          " :: ", "val = ", p2, p1)
                    return(0)



import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

pentagon_numbers()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))