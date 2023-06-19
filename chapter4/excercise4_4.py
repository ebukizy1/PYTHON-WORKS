def mystery (x):
    y = 0
    for i in x:
        if i % 2 == 0:
          y +=i
          return y


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mystery(my_list))