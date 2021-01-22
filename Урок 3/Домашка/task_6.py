def int_funct(text):
    fun_word = text.title()
    return fun_word

word = input('Введите слово ')
word = word.lower()

print(int_funct(word))

worlds = input('Введите слова (через пробел) ')
worlds = worlds.lower()

list_worlds = list(worlds.split())
list_worlds = list(map(int_funct, list_worlds))
worlds = ' '.join(list_worlds)
print(f'Ваши слова {worlds}')