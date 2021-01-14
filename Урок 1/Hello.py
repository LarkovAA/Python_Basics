# коментарии
'''
Я документация для этой программы
'''
price_rub = 500
greatings = f'I am the first program!'
eur_coust = 90
price_eur = price_rub / eur_coust

type_of_veriable = type(price_eur)
print(f'У нас есть: {price_rub} рублей')
print(f'и мы можем купить: {price_rub // eur_coust} евро и {round(price_rub % eur_coust, 2)} евроцентов')
print(type_of_veriable) # проверь на ошибки

if price_eur > 15:
    print('Price to high')
elif price_eur <= 10 and price_eur > 0:
    print('Buy it')
else:
    print('In next month')

while price_eur > 10:
    price_eur -= 0.5
    print(f'Wee update cost:{price_eur}')

while True:
    item = input('What do you want? :')
    if item == 'freedom':
        break
print('You are free!!')


