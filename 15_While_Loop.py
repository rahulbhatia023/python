i = 1
while i <= 5:
    print(i)
    i = i + 1

##########################################

# Program to add natural numbers
# sum = 1+2+3+...+n

n = 10
total = 0

i = 1
while i <= n:
    total = total + i
    i = i + 1

print("The sum is", total)

##########################################

# Example to illustrate the use of else statement with the while loop

counter = 0
while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
