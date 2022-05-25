def fact(x):
   if x==1:
       return 1
   return x*fact(x-1)
x=int(input())
print(fact(x))
print(fact(5))
print(fact(4))
print(fact(8))
#вызываем функцию f(5)=f(4)*5
#f(4)=f(3)*4
#f(3)=f(2)*3
#f(2)=f(1)*2
#f(1) возвращает 1
#1*2 и поднимаемся обратно вверх
