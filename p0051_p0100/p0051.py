'''
the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
with the same digit, is part of an eight prime value family.
E.g. 56003, 56113, 56333, 56443, 56663, 56773, and 56993 for family of 7.
'''
def prime_digit_replacements():
    # for 94063 generate {'n':94063, 1:3, 10:6, 100:0, 1000:4, 10000:9}
    def place_values(n):
        d, pos = {'n':n}, 1
        while(n):
            d[pos] = n % 10
            pos *= 10
            n = n // 10
        return d

    def check_56xx3(pv):
        if pv[1] == 3 and pv[10_000] == 5 and pv[1000] == 6:
            if pv[10] == pv[100]: print(pv)

    # save the matching numbers in a special key to the family
    # for 94063 and ab=[1,100,1000], key = 1101-69
    # first part position value; second part face value of positions
    def check_xx(pv, s1, s2):
        a, b, c = s1[0], s1[1], s1[2]
        res_val = 0
        for x in s2:
            res_val += x*pv[x]
        val = str(a+b+c) + '-' + str(res_val)
        if pv[a] == pv[b] and pv[a] == pv[c]:
            if val in result: result[val].append(pv['n'])
            else: result[val] = [pv['n']]

    # given [0, 2, 3] returns ([1, 100, 1000], [10, 10000]) for 94013
    def ab_combo(ab_pos):
        i, ab, rest = 0, [], []
        for j in ab_pos:
            ab.append(digits[j])      # digits in this set change but same
            rest += digits[i:j]       # digits in this set unchanged for family
            i = j+1
        if i < len(digits): rest += digits[i:]
        return (ab, rest)

    # for 94013 return .... [1, 10, 100, 1000, 10_000]
    def position_values(stop):
        x, pos_val = 1, []
        while(x < stop):       # for stop=100 return [1, 10]
            pos_val.append(x)
            x *= 10
        return pos_val

    # check for all 6 digit numbers (XXX,000)...
    def pdr():
        for x in pset:              # just the 6-digit primes
            pv = place_values(x)    # separate out the digits
            for i in range(len(digits)):    # for each position value
                for j in range(i+1, len(digits)):   # for a second pos value
                    for k in range(j+1, len(digits)):   # for a third ...
                        ab, rest = ab_combo([i, j, k])  # separate out the two parts
                        check_xx(pv, ab, rest)          # check for condition match

    # the main section
    import sys
    sys.path.append('../')
    import common as c

    primes = c.prime_list_generator(1_000_000)
    start, stop = 100_000, 1000_000
    digits = position_values(stop)
    pset = [x for x in range(start, stop) if primes[x]]
    result = {}
    pdr()

    for k in result:
        if len(result[k]) == 8: print("K:V = ", k, result[k])



import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

prime_digit_replacements()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1_000_000))
