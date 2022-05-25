class Student():
    def __init__(self, first_name, last_name):
        """инициализируем атрибуты имя, фамилия, всё вместе"""
        self.name=first_name
        self.surname=last_name
        self.fullname=first_name+' '+last_name
        self.grades=[]
    def greeting(self):
        print('Hello, I am Student '+self.fullname.title())
    def mean_grade(self, grades):
        for i in grades:
            self.grades.append(i)
            a=(sum(map(int,grades)))/len(grades)
        print(a)
s1=Student("Masha", "Smirnova")
print(s1.fullname)
s1.greeting()
s1.mean_grade([3, 4, 5])


