
numbers = 10
for row in range(numbers):
    for colon in range(row):
        print("*",end="")
    print()


for row in range(numbers):
    for colon in range(row, numbers ):
        print("*", end="")
    print()

for row in range(numbers):
    for colon in range(row, numbers):
        print(" ", end="")
    for star in range(row+1):
        print("*", end="")
    print()


for row in range(numbers):
    for colon in range(row):
        print(" ", end="")
    for space in range(row, numbers):
        print("*", end="")
    print()