#решение с помощью рекурсии
#один символ и пустая строка является палиндромом
def is_palindtome(string):
    string=''.join([*filter(str.isalpha, string.lower())])#фильтруем приведя к нижнему регистру и оставляя только буквы
    if len(string) <= 1:  # проверяем длину строки
        return 'YES'
    if string[0] != string[-1]:  # проверяем одинаковые 1 и последнюю букву
        return 'NO'
    return is_palindtome(string[1:-1])  # заново проверяем строку без 1 и последней буквы


print(is_palindtome("Madam, I'm Adam"))
print(is_palindtome("А роза упала на лапу Азора"))
print(is_palindtome('потоп'))
print(is_palindtome('папа'))

2 способ
def is_palindtome(string):
    string=''.join([*filter(str.isalpha, string.lower())])#фильтруем приведя к нижнему регистру и оставляя только буквы
    l=len(string)
    for i in range(l//2):
        if string[i]!=string[-1-i]:
            return 'NO'
    return 'YES'
print(is_palindtome("Madam, I'm Adam"))
print(is_palindtome("А роза упала на лапу Азора"))
print(is_palindtome('потоп'))
print(is_palindtome('папа'))

3 способ
def is_palindtome(string):
    rev_string=''
    string=string.lower()
    wrong=['.', '!', ',', ' ', '?', '-',':', ';', "'"]
    for j in wrong:#удаляем все не нужные знаки и пробелы, получаем 1 строку
        string=string.replace(j, '')
    for i in range(len(string), 0, -1):
        rev_string+=string[i-1]#переварачиваем строку
        if string==rev_string:
            return 'YES'
    return 'NO'
print(is_palindtome("Madam, I'm Adam"))
print(is_palindtome("А роза упала на лапу Азора"))
print(is_palindtome('потоп'))
print(is_palindtome('папа'))

