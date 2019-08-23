'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used? Ignore spaces
'''
def number_letter_count(number=1000):
    # number of letters in the word form, for each value
    dict = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4,
            10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8,
            20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6,
            100:7, 1000:8, 'and':3}

    # numeric representation of the word
    dict2 = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
             6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
             11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
             16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
             20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
             60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',
             100:'hundred', 1000:'thousand', 'and':'and', 0:''}

    def word_filler(word):
        if(word): return(' ')
        else: return('')

    word = ''
    while(number):
        t = number // 1000
        h = (number - t*1000) // 100
        d = (number - t*1000 - h*100) // 10
        u = int(number - t*1000 - h*100 - d*10)

        if(t): word += dict2[t] + ' ' + dict2[1000]
        if(h): word += word_filler(word) + dict2[h] + ' ' + dict2[100]
        if(((t | h) > 0) & ((d | u) > 0)): word += word_filler(word) + dict2['and']
        if(d >= 2): word += word_filler(word) + dict2[d*10]
        if(d == 1): word += word_filler(word) + dict2[d*10 + u]
        else: word += word_filler(word) + dict2[u]

        number -= 1
        #print("nlc_2 = ", num, "[[ ", t, h, d, u, word, " ]]")

    w_len = [len(x) for x in word.split()]
    return(sum(w_len))


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

num = 1000
result = number_letter_count(num)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("Letter count in numbers upto {} = {}".format(num, result))
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
