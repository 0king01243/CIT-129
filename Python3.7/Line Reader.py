names = open('names.txt','r')
lines = names.readlines()

first_names = [i.split()[0] for i in lines]
last_names = [i.split()[1] for i in lines]

for x in range(0, len(lines)):
    print("Good Evening Dr. " + last_names[x] + ", Would you mind if I call you " + first_names[x])

