'''
This comment block was the 2 exercises we did in class
I didn't want to delete them, but didn't feel they deserved their own file
1

numbers = "0123456789"
newFile = open('myFirstFile_sp19.txt', 'w')
for x in range(0, len(numbers)):
    string_1 = numbers[0:len(numbers) - x]
    newFile.write(string_1)
    newFile.write("\n")
newFile.close()

2
names = open('names.txt', 'r')
print(names.readline())

'''

import csv
file = open('jail.csv', newline='')
reader = csv.DictReader(file)
numBlack = 0
numWhite = 0
num28YearsOld = 0
targetDate = '2018-01-01'
valWhite = 'W'
valBlack = 'B'


for row in reader:
    if row['date'] == targetDate:
        if int(row['agecurr']) == 28:
            num28YearsOld = num28YearsOld + 1
        elif row['race'] == valWhite:
            numWhite = numWhite + 1
        elif row['race'] == valBlack:
            numBlack = numBlack + 1
file.close()
print("total 28 year-olds:  " + str(num28YearsOld))
print("num white inmates:  " + str(numWhite))
print("num black inmates:  " + str(numBlack))
percentBlack = (numBlack / (numBlack + numWhite)) * 100
print('percent black inmates:  ' + str(percentBlack) + "%")

