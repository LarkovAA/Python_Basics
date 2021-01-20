# создаем список с рейтингом
rating = [7, 5, 3, 3, 2]
entering_data = int(input('Введите новый рейтинг '))
# сравниваем есть ли значение которое хотим добавить в рейтинге
rating.reverse() # разворачиваем список
for el in rating:
    place = rating.index(el)  # создаем переменную в которой будет содержаться индекс этого же числа в списке
    if el >= entering_data:
        rating.insert(place, entering_data)  # добавляем новое значение рейтинга
        break
    elif entering_data > el and rating[len(rating) - 1] == el: # если наше чисо больше последнего значения в списке
        rating.append(entering_data) # то мы добавляем в коне списка
        break

rating.reverse()
print(f'Ваш новый рейтинг {rating}')
