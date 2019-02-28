db_list = {
    'dict_1': {'name_1': 'TEST11C'},
    'dict_2': {'name_2': 'TEST12C'},
}
name = input("What is the name of the key:   ")

retry_name = ""


def test_dict(x):
    if x in db_list.keys():
            print("You have chosen: " + x)
            return True
    else:
            print('You have chosen wrong!')
            retry_name = input("Please try another name:   ")
            return False


test_dict(name)

while test_dict() == False:
    test_dict(retry_name)

print(name)
