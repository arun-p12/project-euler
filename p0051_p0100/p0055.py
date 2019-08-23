'''
Many numbers such as 47, 349, etc, have a permutation counter part, that when added produces
a palindrome. E.g. 47+74 = 121; 349+943 = 1292 ==> 1292+2921 = 4213 ==> 4213+3124 = 7337

But, some numbers such as 196, or 4996 don't produce a palindrome. These are Lychrel's numbers.
How many such numbers exist below 10,000? Assume max number of iterations = 50
'''
def lychrel_numbers(num=10000):

    def is_palindrome(n):
        if(str(n) == str(n)[::-1]): return(True)
        return(False)

    def next_num(n):
        n_rev = int(str(n)[::-1])
        return(n + n_rev)

    # 0: contains palindromic numbers, while 1: contains the lychrel numbers
    lychrel = {0: {}, 1: {}}
    start = 10
    for i in range(start, num+1):
        n, cnt, ok = i, 1, 1            # save i, keep count of iterations
        while(ok and cnt <= 50):
            n = next_num(n)
            if(is_palindrome(n)): ok = 0
            else: cnt += 1
        lychrel[ok][i] = str(n) + ":" + str(cnt)    # save info, once we exit out of the loop
    print("count = ", len(lychrel[1]))


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

lychrel_numbers()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1_000_000))
