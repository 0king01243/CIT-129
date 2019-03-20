import json
import csv

comparative_dictionary = json.load(open('json_criteria', newline=""))
new_dictionary = {}
file = open("First_Json_file.csv",newline="")
reader = csv.DictReader(file)
comparative_dictionary['status'] = comparative_dictionary['planning_status']
# Have to get the names of the criteria file to match the overall data file
del comparative_dictionary['planning_status']
cleaning_dictionary = comparative_dictionary.copy()

# Deleting all empty criteria to loop over later
for x in cleaning_dictionary:
    if comparative_dictionary[x] == ['']:
        del comparative_dictionary[x]
print(comparative_dictionary)
n = 0

# Creating a dictionary working off of the data that exclusively selected by the first criteria
for x in reader:
    if list(str(comparative_dictionary[list(comparative_dictionary.keys())[0]])[1:][:-1]) == list(x[list(comparative_dictionary.keys())[0]]):
        new_dictionary['entry{0}'.format(n)] = {}
        new_dictionary['entry{0}'.format(n)] = x
        n += 1
del comparative_dictionary[list(comparative_dictionary.keys())[0]]

cleaning_dictionary = new_dictionary.copy()

for entry in range(0, len(comparative_dictionary.keys())):
    for x in cleaning_dictionary.keys():
        if x in new_dictionary:
            xvalue = list(new_dictionary[x][list(comparative_dictionary.keys())[entry]])
            critvalue = list(str(comparative_dictionary[list(comparative_dictionary.keys())[entry]])[2:][:-2])
            if xvalue == critvalue:
                continue
            else:
                del new_dictionary[x]

for x in new_dictionary:
    print(x,':  ',new_dictionary[x])
