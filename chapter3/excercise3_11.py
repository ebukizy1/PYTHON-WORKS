
female_rabbit = int(input("Enter the number of does in the rabbit colony(-1 to end) "))
total = 0
count = 0
while female_rabbit != -1:
    rabbit_born = int(input("Number of baby rabbit born in the past month: "))
    average_rabbit = rabbit_born/ female_rabbit
    print(f" on average {average_rabbit:.1f} baby rabbits were born for each doe")
    total += rabbit_born
    count += 1
    female_rabbit = int(input("Enter the number of does in the rabbit colony(-1 to end"))
average = total / count
print(f"Total number of baby rabbits for each doe so far {average }")