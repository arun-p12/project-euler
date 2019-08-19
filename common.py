########################
###  Get Factors     ###
########################
def get_factors(number):
    factors = []
    i = 1
    while(i <= number / i):
        if(number % i == 0):
            factors.append(i)
            if (i != number / i):
                factors.append(int(number / i))
        i += 1
    #print("factors = ", factors)
    return(factors)

########################
###  Is Prime?       ###
########################
def is_prime(number):
    if(number <= 1): return(False)
    if(number == 2): return(True)
    if((number % 2) == 0): return(False)
    i = 3
    while (i <= int(number**0.5)):
        if (number % i == 0): return(False)
        i += 2
    return(True)

###########################
###  String Permutation ###
###########################
'''
For a string of characters, generate all possible permutations. All characters are used.
E.g. '1103' return ['1103' '1130', '1013', '1031', '1301', '1310', '0113', ... etc]
     it does not return items such as '11', '310' etc.

A slow routine... takes about 7.5s to run... NEED AN ALTERNATE ALGORITHM
'''
def permutation_numbers(string):
    # handle 1-digit and 2-digit numbers.
    if(len(string) == 1): return([string])
    if(len(string) == 2):
        item1 = string[0] + string[1]
        item2 = string[1] + string[0]
        if(item1 == item2): return([item1])
        return([item1, item2])

    # break the number down, cycling thru each digit
    # save the results as a key-value pair .. key = each digit ; value = remaining digits
    my_dict = {}
    for i in range(len(string)):
        my_list = []
        for j in range(len(string)):
            if(i != j): my_list.append(string[j])
        my_dict[string[i]] = my_list

    # use recursion .... repeating for each key, and reducing value to a 2-digit number
    # get the permutation list for each value; prepend it with the key to get the full number
    my_list = []
    for key in my_dict.keys():
        my_list2 = permutation_numbers(my_dict[key])
        for item in my_list2:
            my_list.append(key + item)
    return(my_list)

########################
###  Prime Factors   ###
########################
'''
Generate the list of prime factors of a given number. Also, keep account of the number of
occurances. Works ok for a single number, or a small set of numbers in a loop.
But, highly inefficient for very large set of numbers. Refer problem #47 for an example
'''
def prime_factors(number):
    pf = {}
    x = 2
    while number >= x:
        while (number % x == 0):
            if(x in pf):
                pf[x] += 1
            else:
                pf[x] = 1
            number /= x
        x += 1
    return(pf)

'''
For all the numbers upto N, find its unique prime factors
Note: for 12, 24, and 36, it'll list [2, 3] ... i.e. the unique prime factors
      and not the number of occurances of each
'''
def prime_factors_seive(num):
    p_factors = [[0], [0]]

    # Python lists are mutable objects ... thus, [[]] * (num - 2) won't work
    # Each list in the list woule be a reference to the same object.
    # As we modify one, it gets reflected across all of them. Learnt it the hard way
    # thus, have to use a for loop to create distinct objects

    p_factors += [[] for i in range(num - 2)]
    for i in range(2, num):
        mul = 1
        if(p_factors[i] == []):     # is prime
            while((i * mul) < num):
                p_factors[i * mul].append(i)
                mul += 1
    return(p_factors)


##############################
###  Prime List Generator  ###
##############################
'''
Finally, decided to write a function to return a prime list
Returns either a list of booleans, or       (( [False, False, True, True, ...] vs [2, 3, ...] ))
Returns the list of numeric values of the primes  
'''
def prime_list_generator(num=1000000, bool=1):
    primes = [True for x in range(num)]
    primes[0] = primes[1] = False
    for n in range(2, num):
        if(primes[n]):
            mul = 2
            while((n * mul) < num):
                primes[n * mul] = False
                mul += 1

    if(not bool): primes = [x for x in range(num) if primes[x]]
    return(primes)


