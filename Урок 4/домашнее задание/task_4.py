list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# если значение в списке list находится только 1 раз то мы добавляем это значение в новый список
new_list = [num for num in list if list.count(num) == 1]

print(f'новый список всех значений не имеющих повторений {new_list}')
