number_p = int(input("enter a number"))
firstNumber = 0
secondNumber = 0
thirdNumber = 0
fourthNumber = 0
firstNumber = number_p % 10
number_p = number_p //10
secondNumber = number_p % 10
number_p = number_p // 10
thirdNumber = number_p % 10
number_p = number_p // 10
fourthNumber = number_p % 10
number_p = number_p// 10
if firstNumber == fourthNumber and secondNumber == thirdNumber:
    print("true")
else: print("false")

