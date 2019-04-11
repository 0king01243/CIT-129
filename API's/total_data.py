# This was an early working copy of my government_dataAPI, and it is functional but missing some later updates
# While testing this, try to limit the number of calls you make to less than 1000 per hour, with each loop in the four loop
# Corresponding to 1 call.

import requests
import json

schoolNames = {}
test_url = "https://api.data.gov/ed/collegescorecard/v1/schools?fields=school.name," \
      "latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings,&page=0&api_key=Zxb9DU5BNOoC7n6TDxDdhLJ3M9hx1sJi2dnhAoUv"
test_req = requests.get(test_url)
metadata_api = json.loads(test_req.text)
pages_range = int(metadata_api['metadata']['total'] / metadata_api['metadata']['per_page'])

for x in range(0, pages_range):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?fields=school.name,latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings,&page=" + str(page) + "&api_key=scAsNswP752I4YVVjOd879xhKSfvGQ7a2MToIxO3"
    req = requests.get(url)
    apiDict = json.loads(req.text)
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
