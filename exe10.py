class MyError(Exception):
    def __init__(self, msg):#вызывается при создании экземпляра
        self.msg=msg
    def __str__(self):#при вызове экземпляра на экран.Оператор вызова переводит в состояние ошибки
        return f'Ошибка: {self.msg}'
x=input("Введите число больше или равное 100: ")
try:
    x=int(x)
    if x<100:
        raise (MyError("Значение должно быть больше"))
except ValueError:
    print("Введена не правильная переменная")
except MyError as m:
    print(m)
else:
    print("Число введёно верно:",x)


