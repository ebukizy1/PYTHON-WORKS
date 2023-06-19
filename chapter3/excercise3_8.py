userInput = int(input("Enter the number of reported infections or negative value to exit "))


total = 0
average = 0
smallest = userInput
largest = userInput
counter = + 1
while userInput > 0:
    userInput = int(input("Enter the number of reported infections or negative value to exit "))
    total += userInput
    if userInput > largest:
        largest = userInput
    elif userInput < smallest:
        smallest = userInput
        counter = + 1
        average = total / counter
        print(f"the total of the reported infections patient in a Day is{total} ")
        print(f"the largest number of people receive in a Day is{largest} ")
        print(f"the smallest number of people received in a Day is {smallest} ")
        print(f"the average of the the total patience in a Day is {average} ")


