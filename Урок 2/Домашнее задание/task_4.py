custom_line = input('Введите текст который ходите ? ')
list_custom_line = custom_line.split()

for num, ln in enumerate(list_custom_line, 1):
    if len(ln) <= 10:
        print(f'{num} {ln}')
    else:
        print(f'{num} {ln[ : 10]}')

