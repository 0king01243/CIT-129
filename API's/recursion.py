# Factorials
def factorial(number):
    if number == 1:
        print(number, " = ", end=" ")
        return 1
    else:
        print(number, " * ", end=" ")
        return number * factorial(number-1)


print(factorial(int(input('Which number would you like the factorial of?  '))))


# Pascal's Triangle
def pascal(number):
    if number == 0:
        return [1]
    else:
        line = [1]
        previous_line = pascal(number-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line


x_range = int(input("How many levels would you like to see?  "))
# 27 fills up the whole page
for x in range(0, x_range):
    row = str(pascal(x))[1:][:-1].center(200)
    row = row.replace(",", " ")
    print(row)


'''
Extension Exercise:
 
Use Pascal's Triangle to calculate Fibonacci numbers (These are calculated by adding together all numbers in a diagonal 
starting from the right side up until you hit the left)

'''
