string = "abrakadabra"
str_reverse = ''
symbols = list(string)
for el in range(len(string) // 2 ):
    tmp = symbols[el]
    symbols[el] = symbols[len(string) - el - 1 ]
    symbols[len(string) - el - 1 ] = tmp
    str_reverse = '' .join(symbols)
print(str_reverse)