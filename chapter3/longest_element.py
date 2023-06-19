name = ["emmanuel", "ebuka", "mike"]

def longest_list(lst):
    largest = lst[0]
    for element in lst:
        if len(largest) > len(lst) :
         largest = len(lst)
         return largest


longest_list(name)
print(name)