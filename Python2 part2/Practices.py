#1

for x in range(0,100,2):
    print(x + 1, end=" ")

#2

kaboom_string = "KABOOM"

for x in kaboom_string:
    print((x + " ") * 3, end="")

#3

string_3 = "askaliceithinkshe'llknow"

for x in range(0, len(string_3), 2):
     print(string_3[x:x+1], end=" ")

#4

# ?

#5

listoflists = [['mn', 'pa', 'ut'], ['b', 'p', 'c'], ['echo', 'charlie', 'tango']]
labels = {"state": "US State Abbr:", "element": "Chemical Element:", "alpha": "Phonetic Call:"}

for x in range(0,len(listoflists)):
    print(list(labels.values())[x] + " " + listoflists[x][0].upper())
    print(list(labels.values())[x] + " " + listoflists[x][1].upper())
    print(list(labels.values())[x] + " " + listoflists[x][2].upper())
