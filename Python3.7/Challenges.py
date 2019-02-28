# 1

#for x in range(0,100,2):
#    print(x + 1, end=" ")

#2

#kaboom_string = "KABOOM"

#for x in kaboom_string:
#    print((x + " ") * 3, end="")

#3

#string_3 = "askaliceithinkshe'llknow"

#for x in range(0, len(string_3), 2):
#     print(string_3[x:x+1], end=" ")

#4

# ?

#5

#listoflists = [['mn', 'pa', 'ut'], ['b', 'p', 'c'], ['echo', 'charlie', 'tango']]
#labels = {"state": "US State Abbr:", "element": "Chemical Element:", "alpha": "Phonetic Call:"}

#for x in range(0,len(listoflists)):
#    print(list(labels.values())[x] + " " + listoflists[x][0].upper())
#    print(list(labels.values())[x] + " " + listoflists[x][1].upper())
#    print(list(labels.values())[x] + " " + listoflists[x][2].upper())

#Data Editor

#peer_info = {'Alex': {'Siblings': {'max': 'Oldest', 'Wolfie': 'Youngest'}, 'Pets': 2}, 'Ben': {'Age': 17, 'Pets': 1}, 'Jerry': {'Age': 29, 'Pets': 4}}
#print(peer_info)
#for x in peer_info:
#    start = input("Do you want to edit " + x + ":   ")
#    if start == 'yes' or start == 'y' or start == 'Yes':
#        print(peer_info.get(str(x)))
#        if input("Do you want to edit here or go deeper(edit/deeper):   ") == 'edit':
#            level_2 = input('Which variable would you like to edit:   ')
#            peer_info[str(level_2)] = input("What would you like to change it to?")
#            print(peer_info)

db_list = {
    'dict_1': {'name_1': 'TEST11C'},
    'dict_2': {'name_2': 'TEST12C'},
}
name = input("What is the name of the key:   ")


def test_dict(candidate):
    while candidate not in list(db_list.keys()):
            print('You have chosen wrong!')
            candidate = input("Please try another name:   ")
            if candidate in db_list.keys():
                print("You have chosen: " + candidate)
                print(db_list[str(candidate)])


test_dict(name)
