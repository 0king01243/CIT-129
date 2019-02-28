import csv
file = open("pgh311Abbrev.csv")
reader = csv.DictReader(file)
numCallCenter = 0
numReport2GoviOS = 0
numReport2GovAndroid = 0
numWebsite = 0
numTwitter = 0
numControlPanel = 0

#for x in reader:
#    correct_split = x.split(",")[4]
#    listofrequests.append(correct_split)
#print(listofrequests)

for row in reader:
    if row['REQUEST_ORIGIN'] == "Call Center":
        numCallCenter = numCallCenter + 1
    if row['REQUEST_ORIGIN'] == "Report2Gov iOS":
        numReport2GoviOS = numReport2GoviOS + 1
    if row['REQUEST_ORIGIN'] == "Report2Gov Android":
        numReport2GovAndroid = numReport2GovAndroid + 1
    if row['REQUEST_ORIGIN'] == "Website":
        numWebsite = numWebsite + 1
    if row['REQUEST_ORIGIN'] == "Twitter":
        numTwitter = numTwitter + 1
    if row['REQUEST_ORIGIN'] == "Control Panel":
        numControlPanel = numControlPanel + 1

print(numControlPanel)
print(numTwitter)
print(numWebsite)
print(numReport2GovAndroid)
print(numReport2GoviOS)
print(numCallCenter)

#listofrequests = list(reader)
#print(listofrequests)
