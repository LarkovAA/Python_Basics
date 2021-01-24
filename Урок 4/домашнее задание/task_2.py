from random import randint
from functools import  reduce

list_num = []
while len(list_num) <= 15:
    random_num = randint(0, 1000)
    list_num.append(random_num)

print(list_num)

new_list_num = [num for num in list_num[1:] if num >= list_num[list_num.index(num) - 1]]

print(new_list_num)
