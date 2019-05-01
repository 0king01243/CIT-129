import re
# Lambda Functions

grades = [5,5,7,8,9,5,2,5,3,10,9,6,5]

print(list(filter(lambda x : x >= 8 or x <= 4, grades)))
print(sum(map(lambda x: x / len(grades), grades)))


# Extension 1, did not figure out how to compress into lambda


value = [1,2,3,4,5,6,7,8,9,10]
value_copy = value.copy()
for y in range(0,len(value)):
    for x in range(1,value_copy[y]):
        value_copy[y] -= 1
        value[y] = value[y] * value_copy[y]
print(value)

# try and raise


class myError(Exception):
     pass

try:
    raise myError
except myError:
    print("-executed or not-?")

# Regular Expressions
'''
line = "It was a dark and stormy night"
p = re.compile('(dark)')
m = p.match(line)
print(m.group(1))

'''

line = 'The Stone Sky, by N.K. Jemisin'
p = re.compile(('[a-zA-Z]+'))
m = p.findall(line)
print(m)
print("Title: ", end="")
for x in range(0,3):
    print(m[x],end=" ")
print("", end="\n")
print("Author: ", end=" ")
for x in range(4, 7):
    print(m[x], end=" ")
print("", "\n")


line2 = "  The Stone Sky, by N.K. Jemisin(Orbit)"
p2 = re.compile('[a-zA-Z]+')
m2 = p2.findall(line2)
print(m2)

# Other approach method

publisher = re.compile('\([a-zA-Z]+\)')
match = publisher.match(line2)
print(match)
