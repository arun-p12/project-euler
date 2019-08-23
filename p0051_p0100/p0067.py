'''
Navigating the path from top to bottom of a given triangle ... find the path that
maximizes the sum of the numbers traversed through.
Note: same problem as #18 ... only with a much larger input file
'''
def max_path_sum(file='../p0051_p0100/p0067_path.txt'):
    import sys
    sys.path.append('../p0001_p0050')
    import p0018 as p
    p.max_path_sum(file)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

if __name__ == "__main__":
    max_path_sum()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1_000_000))
