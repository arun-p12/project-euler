'''
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
'''
def counting_sundays(year):
    cal = {}
    start_yr = 1901
    week_day = {1: 'Mon', 2: 'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6:'Sat', 0:'Sun'}
    mon_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    # define a dictionary of dictionaries
    for i in range(start_yr, year+1): cal[i] = {}

    previous = 6                        # what was the 1st day of the previous month (Dec 1900)
    prev_days = 31                      # number of days that month had
    for i in range(start_yr, year+1):
        for j in range(1, 13):
            cal[i][j] = (previous + prev_days) % 7      # get the 1st of this month from previous
            previous = cal[i][j]                        # save the data
            prev_days = mon_days[j]
            if(j == 2):                                 # account for February
                if(i % 400 == 0): prev_days += 1
                elif((i % 4 == 0) & (i % 100 != 0)): prev_days += 1

    sundays = 0
    for k in cal:
        for y in cal[k]:
            #cal[k][y] = week_day[cal[k][y]]            # convert '1' to 'Mon'
            if(cal[k][y] == 0): sundays += 1
    print("sundays = ", sundays)

# easier to read, less scope for error ... but slower
def p19_counting_sundays_2(year=2000, st_yr=1901):
    import datetime

    count = 0
    for y in range(st_yr, year+1):
        for m in range(1, 13):
            if datetime.datetime(y, m, 1).weekday() == 6: count += 1    # sunday = 6; mon is 0
    print("cs_2 = ", count)

# same as above ... using list comprehension
def p19_counting_sundays_3(year=2000, st_yr=1901):
    from calendar import weekday
    print("cs_3 = ", sum(int(weekday(y, m, 1) == 6) for y in range(st_yr, year+1)
                         for m in range(1, 13)))

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

counting_sundays(2000)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
