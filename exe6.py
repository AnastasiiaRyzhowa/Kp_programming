def calculatE(path2file):
    with open(path2file, 'r') as f:
        l = []
        res = []
        for i in f.readlines():
            l.append(i.replace('\n', '').split())#берем 1 строку и делаем из неё список сохраняя в l
        for i in l:#перебираем каждое значение
             try:
                 if i[0] == '+':
                     res.append(str(int(i[1]) + int(i[2])))#сохраняем значение в результаты
                 elif i[0] == '-':
                     res.append(str(int(i[1]) - int(i[2])))
                 elif i[0] == '*':
                     res.append(str(int(i[1]) * int(i[2])))
                 elif i[0] == '//':
                     res.append(str(int(i[1]) // int(i[2])))
                 elif i[0] == '%':
                     res.append(str(int(i[1]) % int(i[2])))
                 elif i[0] == '**':
                     res.append(str(int(i[1]) ** int(i[2])))
             except (IndexError, ZeroDivisionError, ValueError) as e:#обработка исключений при некорректном вводе
                 print(e)
        return (','.join(res))
print(calculatE('t2.txt'))

