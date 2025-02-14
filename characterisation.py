import  pandas as pd

'''
character prototype
artributes:
types
- protagonist
- antagonist
- neutral
- Zelous
- window

- get the dataframe for the object

 - make dataframe method
'''
name_list=[]
type_list=[]

class Character():
    def __init__(self, mytype, myname):
        self.type=mytype
        self.name=myname

    # class method
    def generate_dataframe (self):
         type_list.append(self.type)
         name_list.append(self.name)

# data inputation
character1= Character('protagonist', 'roland')
character2= Character('pawn', 'lazarus')
character3= Character('zelous', 'baladan')
character4= Character('window', 'zorayr')
character5= Character('neutral', 'rio jerecho')

# calling the characters

character1.generate_dataframe()
character2.generate_dataframe()
character3.generate_dataframe()
character4.generate_dataframe()
character5.generate_dataframe()

# create headers
column_headers=['Archetype', 'Name']

# generate dataframe
df = pd.DataFrame(list(zip(type_list ,name_list)),columns=column_headers)

# save input file
df.to_csv('character.csv', index=False)
