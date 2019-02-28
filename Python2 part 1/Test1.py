main = {}

y = int(input("How many siblings do you have:   "))

for x in range(0,y):
        main[str(input("What is your Sibling's Name:   "))] = {'Age': input("What is their Age:   "),'Birthday': input("When is their Birthday:   ")}

print(main)

