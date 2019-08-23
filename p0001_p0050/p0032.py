'''
7254 = 39 x 186, where the multiplicand, the multiplier, and the product combine to make a
1 to 9 pandigital number  [[ all digits from 1-9 used, and used only once ]]
What is the sum of the products of all combinations of such combinations?
'''

# get the list of pandigital triplet ... save it as a dict, keyed on product; eliminate duplicates
def pd_product(x, y):
    # for verification returning the prod, the multiplicand, and the multiplier
    # since the final task is the find the sum of the products ... k=0 has the discard pile
    k, key, prod, target = 0, {}, (x * y), list('123456789')
    if(sorted(str(prod) + str(x) + str(y)) == target): k = prod
    key[k] = [x, y]
    return(key)

'''
Since the required set is 1-9 pandigital, a zero should not be contained in the multiplicand, 
the multiplier, or the product. Additionally, all digits must be different. There are only
two combinations i) a 1-digit number multipled by a 4-digit number resulting in a 4-digit
product ii) a 2-digit number multipled by a 3-digit number resulting in a 4-digit
product.
'''
def pandigital_products():
    pandigital = {}

    # A * BCDE = WXYZ       (product = 4-digit number)
    for a in range(2, 10):                          # can ignore 1
        for abcd in range(1234, int(10000/a)+1):    # anything below either has a 0, or a repeat
            pandigital.update(pd_product(a, abcd))  # anything above results in a 5-digit product

    # AB * CDE = WXYZ   (product = 4-digit number)
    for ab in range(12, 100):                       # smallest non repeating 2-digit number
        for cde in range(123, int(10000/ab)+1):     # anything above results in a 5-digit product
            pandigital.update(pd_product(ab, cde))

    sum = 0
    for k in pandigital.keys():
        sum += k
    print("sum = ", sum, pandigital)

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

pandigital_products()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
