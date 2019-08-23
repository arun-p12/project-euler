'''
If right triangles are formed, with each side having interger values; what is the value of
the perimeter P, that would have the largest set of such right triangles.
E.g. 120 can be formed by :: {20,48,52}, {24,45,51}, {30,40,50}
'''

def int_rt_triangles(num, start=12):
    import math
    max, max_p, result = 0, 0, {}
    for a in range(1, int(num / 2)):
        for b in range(a, int(num / 2)):
            c = int(math.sqrt(a * a + b * b))
            if((((a**2) + (b**2)) == c**2) and (a + b + c <= num)):
                val = str(a) + ":" + str(b) + ":" + str(c)
                if(a+b+c in result.keys()): result[a+b+c].append(val)
                else: result[a+b+c] = [val]

    for key in sorted(result.keys()):
        key_len = len(result[key])
        if(key_len > max): (max, max_p) = (key_len, key)
        #print("max = ", max_p, max, " :: ", key, key_len, result[key])
    print("max perimeter = ", max_p, "len = ", max)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

int_rt_triangles(1000)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
