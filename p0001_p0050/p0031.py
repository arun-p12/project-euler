'''
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p = £2
How many different ways can £2 be made using any number of coins?
'''

# an ugly as sin brute force method.
def total_pounds(amount):
    # for each denomination determine the max # of coins, and the value of those many coins.
    denom = [1, 2, 5, 10, 20, 50, 100, 200]
    denom_max = [200, 100, 40, 20, 10, 4, 2, 1]
    denom_vals = {1: [], 2: [], 5: [], 10: [], 20: [], 50: [], 100: [], 200: []}
    results = {}
    for d in denom:
        index = denom.index(d)
        for c in range(denom_max[index] + 1):
            denom_vals[d].append(d * c)

    # for each value from each of the sets, find the combo resulting in £2.
    # Ignore all additional values of the set, if the amount is excessive.
    counter = 0
    for one_p in denom_vals[1]:
        for two_p in denom_vals[2]:
            if((one_p + two_p) > 200): break
            for five_p in denom_vals[5]:
                if ((one_p + two_p + five_p) > 200): break
                for ten_p in denom_vals[10]:
                    if ((one_p + two_p + five_p + ten_p) > 200): break
                    for twenty_p in denom_vals[20]:
                        if ((one_p + two_p + five_p + ten_p + twenty_p) > 200): break
                        for fifty_p in denom_vals[50]:
                            if ((one_p + two_p + five_p + ten_p + twenty_p + fifty_p) > 200): break
                            for oneh_p in denom_vals[100]:
                                if ((one_p + two_p + five_p + ten_p + twenty_p + fifty_p + oneh_p) > 200): break
                                for twoh_p in denom_vals[200]:
                                    if ((one_p + two_p + five_p + ten_p + twenty_p + fifty_p + oneh_p + twoh_p) > 200): break
                                    if((one_p + two_p + five_p + ten_p + twenty_p +
                                    fifty_p + oneh_p + twoh_p) == amount):
                                        #results.add([one_p, two_p, five_p, ten_p, twenty_p,
                                        #             fifty_p, oneh_p, twoh_p])
                                        results[counter] = [one_p, two_p, five_p, ten_p,
                                                            twenty_p, fifty_p, oneh_p, twoh_p]

                                        #print(counter, results[counter])
                                        counter += 1

    print("count = ", counter)

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

total_pounds(200)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))