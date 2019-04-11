import requests
import json

schoolNames = {}
page = 0
# This code is used to determine how many calls need to be made to include the whole data set

test_url = "https://api.data.gov/ed/collegescorecard/v1/schools?fields=school.name," \
      "latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings,&page=0&api_key=Zxb9DU5BNOoC7n6TDxDdhLJ3M9hx1sJi2dnhAoUv"
test_req = requests.get(test_url)
metadata_api = json.loads(test_req.text)
pages_range = int(metadata_api['metadata']['total'] / metadata_api['metadata']['per_page'])
# This function makes 358 calls every time it is run, and the request limit per hour is 1000.
# If you overuse this API key, one other key is scAsNswP752I4YVVjOd879xhKSfvGQ7a2MToIxO3f
# If you want to use this key, please change it in the URL
# In the future, I would add a prompt at the beginning prompting for an API key, so users could use their own.
for x in range(0, pages_range):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?fields=school.name,latest.earnings." \
          "10_yrs_after_entry.working_not_enrolled.mean_earnings,&page=" + str(page) + "&api_key=Zxb9DU5BNOoC7n6TDxDdhLJ3M9hx1sJi2dnhAoUv"
    req = requests.get(url)
    apiDict = json.loads(req.text)
    page += 1
    for y in apiDict['results']:
        schoolNames[y['school.name']] = y['latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings']

# Had to create a copy of school names, because I couldn't loop over a dictionary while deleting some of its keys
delete_empty = schoolNames.copy()
for x in delete_empty:
    if delete_empty[x] is None:
        del schoolNames[x]

# Sorted function puts the schools in order from lowest mean income to highest
# This was done in order to see what kinds of schools rank at the top and bottom
sortedSchool = {}
for x in sorted(schoolNames, key=schoolNames.get):
    sortedSchool[x] = schoolNames[x]

for x in sortedSchool:
    print(x, end="  ")
    print(sortedSchool[x], end="\n")

# After weeding out all entries that did not have data, I added together all of the income from these schools, then divided by the number
# Of items in the list to get the average
running_total = 0
for x in schoolNames:
    running_total = running_total + schoolNames[x]
average = running_total / len(schoolNames)

# This statement was added to show how many schools data were collected on
print("For the ", len(schoolNames), " schools in our database,",end="\n")
print("The average income of a college student 10 years after graduating is: " + str(average))


# This is a simple search function implemented so users do not have to ctrl + f to find everything
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
