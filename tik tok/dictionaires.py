def key_values(name, dic_age):
    if name in dic_age:
        return dic_age[name]
    else:
        return "the age is not found in the dictionary"


name = input("Enter your name to find your age:")
dic_age = {"segun": 32, "mikel": 17, "david": 26}
values = key_values(name, dic_age)
print(values)