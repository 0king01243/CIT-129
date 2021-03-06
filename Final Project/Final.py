db_list = {
    'dict_1': {'name_1': 'TEST11C','name_3': 'tesasdgasd'},
    'dict_2': {'name_2': 'TEST12C'},
}
# This line was made to create a restore point for the user to return to.
db_backup = db_list.copy()

# This function was designed to check if a dictionary the entered was in our data, and have them repeat until it was.
def test_dict(candidate):
    while candidate not in list(db_list.keys()):
            print('Name does not exist')
            candidate = input("Please try another name:   ")
            if candidate in db_list.keys():
                print("You have chosen: " + candidate)
                return candidate
    return candidate


def editor():
    key = test_dict(input("What dictionary would you like to enter:  "))
    print(db_list[key])
    if len(db_list[key]) <= 1:
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


def insert_option():
    insert = test_dict(input("What dictionary would you like to enter:   "))
    new_key = input("What should the new key name be:  ")
    new_value = input("What should the new value be:   ")
    db_list[str(insert)][new_key] = new_value


def delete_option():
    level = input("Do you want to delete a dictionary or empty it(d/e) ")
    if level == 'e':
        delete = input("Which dictionary do you want to enter:   ")
        db_list[str(test_dict(delete))] = {}
    elif level == 'd':
        delete = input("Which dictionary would you like to delete")
        del db_list[str(test_dict(delete))]


def reset_option():
    double_check = input("Are you sure you want to reset the dictionary(y/n)   ")
    if double_check == 'y':
        global db_list
        db_list = db_backup.copy()
    elif double_check == 'n':
        return

# The main function loops over itself until the user inputs 6, so they are asked everytime they do an action which action to do next.
def main():
    print(db_list)
    movement = input("Would you like to: \n 1: Edit an Entry \n 2: Insert an Entry \n 3: Delete/Empty a Dictionary \n 4: Create a dictionary \n 5: Return Dictionary to starting values \n 6: Quit the program \n")
    if movement == "1":
        editor()
        main()
    elif movement == "2":
        insert_option()
        main()
    elif movement == "3":
        delete_option()
        main()
    elif movement == "4":
        db_list[str(input("What should the name of the dictionary be:  "))] = {}
        main()
    elif movement == "5":
        reset_option()
        main()
    elif movement == "6":
        quit()
    else:
        print("Please select an appropriate value")
        main()


main()
