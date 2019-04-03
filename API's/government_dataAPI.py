import requests
import json

schoolNames = {}
page = 0
# 358
for x in range(0, 358):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?fields=school.name,latest.earnings." \
          "10_yrs_after_entry.working_not_enrolled.mean_earnings,&page=" + str(page) + "&api_key=scAsNswP752I4YVVjOd879xhKSfvGQ7a2MToIxO3"
    req = requests.get(url)
    apiDict = json.loads(req.text)
    page += 1
    for y in apiDict['results']:
        schoolNames[y['school.name']] = y['latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings']

delete_empty = schoolNames.copy()
for x in delete_empty:
    if delete_empty[x] is None:
        del schoolNames[x]

sortedSchool = {}
for x in sorted(schoolNames, key=schoolNames.get):
    sortedSchool[x] = schoolNames[x]

for x in sortedSchool:
    print(x, end="  ")
    print(sortedSchool[x],end="\n")
running_total = 0
for x in schoolNames:
    running_total = running_total + schoolNames[x]

average = running_total / len(schoolNames)
print("The average income of a college student 10 years after graduating is: " + str(average))

while True:
    searching = input('Would you like to search for a college by full school name(y/n):  ')
    if searching == 'y':
        search = input('Which college would you like to search for:  ')
        if str(search) in sortedSchool:
            print("The average income of a student 10 years after graduating is ", sortedSchool[search])
        else:
            print('That school does not exist in our database.')
    else:
        quit()
