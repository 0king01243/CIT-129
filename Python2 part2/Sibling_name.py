main = {}
name = ''
birthday = ''
peer_info = {'name': name, 'birthday': birthday}
key_list = list(peer_info.keys())

for x in key_list:
        sibling_name = input("What is your Sibling's Name:   ")
        main["Sibling"] = {'Age': input("What is their Age:   "), 'Birthday': input("When is their Birthday:   ")}
        main[str(sibling_name)] = main["Sibling"]
        del main["Sibling"]
print(main)
