# Break Statement:

for number in range(1, 11):
    if number == 5:
        break  # break here
    print('Number is ' + str(number))
print('Out of loop')

#####################################################################

# Continue Statement:

for number in range(1, 11):
    if number == 5:
        continue  # continue here
    print('Number is ' + str(number))
print('Out of loop')

#####################################################################

# Pass Statement

for number in range(1, 11):
    if number == 5:
        pass
    print('Number is ' + str(number))
print('Out of loop')

# The pass statement occurring after the if conditional statement is telling the program to continue to run the loop
# and ignore the fact that the variable number evaluates as equivalent to 5 during one of its iterations.
