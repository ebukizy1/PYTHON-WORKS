def addition(number1, number2):
    return number1 + number2


def substraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 / number2


class Calculator:

    def calculator(self, number1, number2, operator):
        match operator:
            case '+':
                addition(number1,number2)
            case '-':
                substraction(number1, number2)
            case '*':
                multiplication(number1, number2)
            case '//':
                division(number1, number2)


print(Calculator.calculator(23, 54, '+'))

