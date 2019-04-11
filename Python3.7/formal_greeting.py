names = open('names.txt','r')
lines = names.readlines()

first_names = []
last_names = []

for x in lines:
    splits = x.split(" ")
    first_names.append(splits[0])
    # I had to split the last name by :-1 in order to remove the \n character
    last_names.append(splits[1][:-1])

for x in range(0, len(lines)):
    print("Good Evening Dr. " + last_names[x] + ", Would you mind if I call you " + first_names[x])

