'''
TASK
1. Print the XML version and encoding of the file
2. Print the root tag
3. Write a for loop to iterate through the child elements of the root element and print all the pairs of child tags and child attributes.
4. Print the child elements whose attributes are empty

'''

import xml.etree.ElementTree as ET

tree = ET.parse ('file.xml') 

root = tree.getroot()   


########################## The actual solution to the tasks is below

#Question 1
with open ('file.xml', 'r') as rf:
    for line in rf:
        if 'version' and 'encoding' in line:
            print (line)


# Question 2
print (root.tag)

# # Question 3


for child in root:
    print(child.tag, child.attrib)


# Question 4

for x in root:
    if x.attrib == {}:
        print (x)
