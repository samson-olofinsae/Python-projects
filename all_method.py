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
# Using a function
def mybase():
    if all(ch in 'ATCG' for ch in sequence):
        print('TRUE')    
    else:
        print('FALSE')
mybase()
##  OR
def validate_sequence(sequence):
    if not all(base in 'ATCG' for base in sequence):
        return False
    else:
        return True
########### Unite testing
########### write your unittest first

class TestBaseFunction(unittest.TestCase):
    def test_my_base(self):
        input_sequence='ATCGGi'
        expected_output=True
        myinput=mybase(input_sequence)
        self.assertEqual(expected_output, myinput)        

if __name__=='__main__':
    unittest.main()
