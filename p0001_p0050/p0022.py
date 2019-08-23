'''
Given a list of names, what is the sum of (the product of (the position of the name in the list
and (the sum of the positional values of the alphabets the name is made of)))
E.g. A, BCD  should give  1x1 + 2(2+3+4) = 19
'''
def read_file(file):
    import re
    name_list = [line.strip().split(',') for line in open(file, "r").readlines()]
    n_list = []
    names = str(name_list)
    names = re.sub('["\[\]\',]', '', names)     # strip off characters: "[],'
    return(names.split())

    #for name in name_list:
    #    s = str(name).replace('"', '')
    #    print("s = ", s)
    #    n_list.append(s)

    #return(n_list)

def name_score_sum(file):
    # create dictionary of characters, and their numeric equivalent
    def ch_dict():
        dict = {}
        i = 1
        for ch in range(ord('A'), ord('Z') + 1):
            dict[chr(ch)] = i
            i += 1
        return(dict)

    # add up the score for the given name
    def name_score(name):
        score = 0
        for ch in name: score += dict[ch]
        return(score)

    dict = ch_dict()
    names = read_file(file)
    names.sort()
    sum_score = 0
    for x in range(0, len(names)):
        score = name_score(names[x])
        #print("names = ", names[x], score, x+1, (score * (x+1)))
        sum_score += (score * (x+1))
    print("name score sum = ", sum_score)

def name_score_sum_2(file):
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    line = open(file, "r").readline().strip()                       # read the whole line
    num = 0
    name = sorted([i.strip("\"") for i in list(line.split(","))])   # split it, strip off ", and sort
    l = 0
    for i in name:
        l += 1
        num += l * sum([A.index(i[k]) + 1 for k in range(len(i))])
    print("name score sum = ", num)

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

file = './p0022_names.txt'
name_score_sum(file)
name_score_sum_2(file)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
