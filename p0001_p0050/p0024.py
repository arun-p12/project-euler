'''
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

# the original code, ugly as sin
def lexographic_permutation(number):
    digits = range(0, 10)
    taken = []
    counter = 0
    # list(set(digits) - set(taken))
    for a in digits:
        taken.append(a)
        for b in [item for item in digits if item not in taken]:
            taken.append(b)
            for c in [item for item in digits if item not in taken]:
                taken.append(c)
                for d in [item for item in digits if item not in taken]:
                    taken.append(d)
                    for e in [item for item in digits if item not in taken]:
                        taken.append(e)
                        for f in [item for item in digits if item not in taken]:
                            taken.append(f)
                            for g in [item for item in digits if item not in taken]:
                                taken.append(g)
                                for h in [item for item in digits if item not in taken]:
                                    taken.append(h)
                                    for i in [item for item in digits if item not in taken]:
                                        taken.append(i)
                                        for j in [item for item in digits if item not in taken]:
                                            counter += 1
                                            #print(a, b, c, d, e, f, g, h, i, j)
                                            if(counter == number):
                                                print("number = ", a, b, c, d, e, f, g, h, i, j)
                                                return(0)
                                        taken.remove(i)
                                    taken.remove(h)
                                taken.remove(g)
                            taken.remove(f)
                        taken.remove(e)
                    taken.remove(d)
                taken.remove(c)
            taken.remove(b)
        taken.remove(a)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############
number = 1000000
lexographic_permutation(number)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
