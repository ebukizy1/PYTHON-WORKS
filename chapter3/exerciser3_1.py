passed = 0
failed = 0
grades  = int(input("enter either 1-> passed or 2-> failed or -1 to exit"))

while grades != -1:
    grades = int(input("enter either 1 -> student passed or 2-> student failed"))
    if grades == 1:
        passed = passed + 1
    else:
        failed = failed + 1

if passed >= 8:
 print("bonus to instructor")
print(f"the total number of student that passed is{passed}")
print(f"the total number of student that failed is{failed}")
