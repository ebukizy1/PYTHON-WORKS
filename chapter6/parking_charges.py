# todo

def parking_garage(hour):
    minimum_charges = 2.00
    additional_charges = 0
    excess = 0.50
    extra_charges = 0
    maximum_charges = 24
    if hour <= 3:
        return minimum_charges
    if 3 < hour <= 23:
        additional_charges = hour - 3
        extra_charges = additional_charges * minimum_charges
        new_charges = extra_charges + minimum_charges
        return new_charges
    if hour == 24:
        return maximum_charges


customer = int(input("Enter the numbers of customer"))
count = 1
while count <= customer:
    hour = int(input("Enter the number of hours for customer "))
    charges = parking_garage(hour)
    print(charges)

