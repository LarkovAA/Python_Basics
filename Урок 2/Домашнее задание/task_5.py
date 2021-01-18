# создаем список с рейтингом
rating = [7, 5, 3, 3, 2]
entering_data = int(input('Введите новый рейтинг '))
# сравниваем есть ли значение которое хотим добавить в рейтинге
if entering_data in rating: # если да то выполняем данный блок
    rating.reverse() # разворачиваем список
    place = rating.index(entering_data) # создаем переменную в которой будет содержаться индекс этого же числа в списке
    rating.insert(place, entering_data) # добавляем новое значение рейтинга
    rating.reverse() # снова разворачиваем список
else:
    rating.reverse() # переворачиваем список
    for num in rating: #  проходим по каждому значению списка
        if entering_data < num: # если введенное значение меньше элемента списка
            place = rating.index(num) # добавляем в переменную значение индекса числа в списке
            rating.insert(place, entering_data) # добавляем новое значение в список
            rating.reverse()
            break
        elif entering_data > num and rating[len(rating) - 1] == num: # если наше чисо больше последнего значения в списке
            rating.append(entering_data) # то мы добавляем в коне списка
            rating.reverse()
            break

print(f'Ваш новый рейтинг {rating}')
