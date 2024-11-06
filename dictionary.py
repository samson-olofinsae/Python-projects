# A dictionary of monthly events

november= {'week1': {'day1':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},


                'day2':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day3':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day4':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day5':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''}},



        'week2': {'day1':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},


                'day2':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day3':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day4':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day5':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''}},



        'week3': {'day1':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},


                'day2':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day3':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day4':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day5':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''}},


        'week4': {'day1':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},


                'day2':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day3':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day4':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''},

                'day5':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':''}}}










# syntax: 
# calling an event: print(month['week']['day]['hour])
# updating an event: month['week']['day'].update({'hour':'new event'})
# calling updated event: print(month['week']['day']['hour'])


# checking the event in nov week2, day3
#print(nov['week2']['day3']['9-10'])

# updating events in nov, week2, day3
november['week2']['day3'].update({'9-10':'designing calender dictionary'})
november['week2']['day3'].update({'10-11':'designing calender dictionary'})
november['week2']['day3'].update({'11-12':'designing calender dictionary'})


# checking the updated events 
print(november['week2']['day3']['9-10'])
print(november['week2']['day3']['10-11'])
print(november['week2']['day3']['11-12'])

