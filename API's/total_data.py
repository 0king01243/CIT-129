import requests
import json

schoolNames = {}
page = 0
# 358
for x in range(0, 3):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?fields=school.name,latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings,&page=" + str(page) + "&api_key=scAsNswP752I4YVVjOd879xhKSfvGQ7a2MToIxO3"
    req = requests.get(url)
    apiDict = json.loads(req.text)
    page += 1
    for y in apiDict['results']:
        schoolNames[y['school.name']] = y['latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings']

delete_empty = schoolNames.copy()
for x in delete_empty:
    if delete_empty[x] is None:
        del schoolNames[x]

sortedSchool = [(k, schoolNames[k]) for k in sorted(schoolNames, key=schoolNames.get)]
for x in sortedSchool:
    print(x,end="\n")

running_total = 0
for x in schoolNames:
    running_total = running_total + schoolNames[x]


average = running_total / len(schoolNames)
print(average)
