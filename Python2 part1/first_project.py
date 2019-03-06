main = {}

y = int(input("How many siblings do you have:   "))

for x in range(0,y):
        sibling_name = input("What is your Sibling's Name:   ")
        main["Sibling{0}".format(x + 1)] = {'Age': input("What is their Age:   "),'Birthday': input("When is their Birthday:   ")}
        main[str(sibling_name)] = main["Sibling{0}".format(x + 1)]
        del main["Sibling{0}".format(x + 1)]
print(main)
