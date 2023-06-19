
number = int(input("enter a number"))
sum_of_divisor = 0
for i in range(1, number):
    if number % i == 0:
        sum_of_divisor+= i
        print(i)
if sum_of_divisor == number:
    print("it is a perfect number")
else: print(" it is not a perfect")



