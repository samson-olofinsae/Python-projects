# A dictionary of monthly events

import collections
from collections import OrderedDict
import pandas as pd

nov= {'week1': {'day1':{'9-10':'work', '10-11':'eat','11-12':'work','12-1':'work','1-2':'work',
                        '2-3':'work','3-4':'work','4-5':'closing'},

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
                        '2-3':'work','3-4':'work','4-5':'nothing yet'},

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
# calling an event: print(month['week']['day']['hour'])
# updating an event: month['week']['day'].update({'hour':'new event'})
# calling updated event: print(month['week']['day']['hour'])
# calling all events of certain day in a certain week: print(nov['week']['day'])


# checking the event in nov week2, day3
#print(nov['week2']['day3']['2-3'])

# updating events in nov, week2, day3
nov['week2']['day3'].update({'9-10':'designing calender dictionary'})
nov['week2']['day3'].update({'10-11':'designing calender dictionary'})
nov['week2']['day3'].update({'12-1':'praying to the Lord'})

nov['week2']['day3'].update({'1-2':'praying to the Lord, lunch break'})
nov['week2']['day3'].update({'2-3':'studing dictionary'})
nov['week2']['day3'].update({'3-4':'studying list and string'})
nov['week2']['day3'].update({'4-5':'studying list and string'})

# UPDATING
#nov['week2']['day3'].update({'2-3':'Finished eating, thinking, '})

#nov['week2']['day3'].update({'2-3':'Finished eating ,thinking, '})

# checking the updated events 
# print(nov['week2']['day3']['1-2'])
# print(nov['week2']['day3']['2-3'])
# print(nov['week2']['day3']['3-4'])
# print(nov['week2']['day3']['4-5'])

# retriving key-value pair for a dictionary of interest from a nested dictionary

# syntax: print(month['week']['day'])


my_interest_dict=nov['week1']['day1']
#print(my_interest_dict)

#print(type(my_interest_dict))
for x, y in my_interest_dict.items():
    pass
    #print(x,y)

# WEEK3, DAY4
#print(nov['week3']['day4'])


# checkiing event in week2, day4, 9-10
#print(nov['week2']['day4']['9-10'])

# updating the event
#print(nov['week2']['day4'].update({'4-5':'python'}))

#print(nov['week2']['day4']['9-10'])
#print(nov['week2']['day4']['4-5'])


## WORKING ON PANDAS

###################
# pratical dataframe : converting dictionary objects to list and to pandas dataframe

####################################################

print(nov['week2']['day4'].keys())
print(nov['week2']['day4'].values())

time_list=[]
activity_list=[]

for time in nov['week2']['day4'].keys():
    #print(key)
    time_list.append(time)

for activity in nov['week2']['day4'].values():
    #print(activities)
    activity_list.append(activity)


#print(time_list)
#print(activity_list)

#master_list=[time_list, activity_list]
#print(master_list)


######### using zip
# I use zip to zip the two lists
# list of strings

# both lists, with columns specified

# creating the initial dataframe

column_headers=['hour', 'activities']
#df = pd.DataFrame(list(zip(time_list ,activity_list)),columns=['hour', 'activiies'])
df = pd.DataFrame(list(zip(time_list ,activity_list)),columns=column_headers)

# insert column heading 'day' to the 0th index of the dataframe and insert 'day1'
df.insert(0, 'day', 'day4')

df.to_csv('week2_day4_activity.csv', index=False)
