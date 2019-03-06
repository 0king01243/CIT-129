db_list = {
    'dict_1': {'name_1': 'TEST11C', "name_2": 'TEST11D'},
    'dict_2': {'name_2': 'TEST12C'},
}
#name = input("What is the name of the key:   ")

#retry_name = ""


#def test_dict(x):
#    if x in db_list.keys():
#            print("You have chosen: " + x)
#            return True
#    else:
#            print('You have chosen wrong!')
#            retry_name = input("Please try another name:   ")
#            return False


#test_dict(name)

#while test_dict() == False:
#    test_dict(retry_name)

#print(name)


def editor():
    key = input("What dictionary would you like to enter:  ")
    print(db_list[key])
    if len(db_list[key]) == 1:
        new_name = input("What would you like to rename the key:  ")
        db_list[new_name] = {new_name: input("What would you like the new value to be:   ")}
        db_list[key] = db_list[new_name]
        del db_list[new_name]
    else:
        old_key = input("Which key would you like to replace:  ")
        new_key = input("What should its new name be:  ")
        new_value = input("What do you want its value to be:   ")
        db_list[key][str(new_key)] = new_value
        db_list[key][str(old_key)] = db_list[key][str(new_key)]
        del db_list[key][str(old_key)]


editor()
print(db_list)
