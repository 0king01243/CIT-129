import os

path = input("What is the path you would like to go to:   ")

while True:
    os.chdir(path)
    os.makedirs(input("What directory would you like to make"))
    if input("Would you like to make another directory (yes/no):   ") == "yes":
        if input("Would you like to change the path (yes/no):   ") == "yes":
            path = input("What is the path you would like to go to:   ")
    else:
        quit()
