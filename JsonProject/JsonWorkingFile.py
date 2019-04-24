import json
import csv

comparative_dictionary = json.load(open('json_criteria', newline=""))
new_dictionary = {}
#print(comparative_dictionary)
file = open("First_Json_file.csv",newline="")
reader = csv.DictReader(file)
comparative_dictionary['status'] = comparative_dictionary['planning_status']
del comparative_dictionary['planning_status']
cleaning_dictionary = comparative_dictionary.copy()


#for x in comparative_dictionary:
#    print(x)

for x in reader:
    print(x)

for x in cleaning_dictionary:
    if comparative_dictionary[x] == ['']:
        del comparative_dictionary[x]

n = 0
for x in reader:
    if list(str(comparative_dictionary[list(comparative_dictionary.keys())[0]])[1:][:-1]) == list(x[list(comparative_dictionary.keys())[0]]):
        new_dictionary['entry{0}'.format(n)] = {}
        new_dictionary['entry{0}'.format(n)] = x
        n += 1
del comparative_dictionary[list(comparative_dictionary.keys())[0]]


#print(new_dictionary[list(new_dictionary.keys())[0]]['start_date'])
#print(new_dictionary['entry0']['start_date'])
#print(list(comparative_dictionary.keys())[0])

#for x in new_dictionary[list(new_dictionary.keys())[0]].keys():
#    print(new_dictionary[list(new_dictionary.keys())[0]][x])
cleaning_dictionary = new_dictionary.copy()
entry = 0
for x in cleaning_dictionary.keys():
    if list(new_dictionary[x][list(comparative_dictionary.keys())[entry]]) == list(str(comparative_dictionary[list(comparative_dictionary.keys())[entry]])[2:][:-2]):
        print('sweet')
    else:
        print('nope')
#    else:
#        if n < len(comparative_dictionary.keys()):
#            n += 1
#print(list(new_dictionary['entry0'][list(comparative_dictionary.keys())[entry]]))
#print(list(str(comparative_dictionary[list(comparative_dictionary.keys())[entry]])[2:][:-2]))


