# Using the all() method
# iterable # tupple, dictionary, list
# syntax all(iterable)

sequence = 'ATTTGC'


if all(ch in 'ATCG' for ch in sequence):
    print('TRUE')
    
else:
    print('FALSE')

# explaination
''' 
for every character (ch) in the variable 'sequence'; 
if the character is in the letters ATCG;
print TRUE; 
otherwise print FALSE
'''
