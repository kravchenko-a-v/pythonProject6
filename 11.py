class Person:
    def __init__(self, name, lastname, age):
        self.__name = name
        self.__lastname = lastname
        self.__age = age

    def say_hello(self):
        print(f'hello my name is {self.__name}')

    def info(self):
        print(f'name = {self.__name}, age = {self.__age}, '
              f'lastname = {self.__lastname}')

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if isinstance(age, str):
            try:
                age = int(age)
            except Exception:
                age = 2

        if age > 0 and age <100:
            self.__age = age
        else:
            self.__age = 0

    def get_age(self):
        return self.__age

def older(li, age):
    li1 = []
    for p in li:
        if p.get_age() > age:
            li1.append(p)
    return li1

li = []
person = Person('Ivan', 'Ivanov', 20)
li.append(person)
person = Person('Ivan', 'Petrov', 14)
li.append(person)
person = Person('Petr', 'Ivanov', 22)
li.append(person)
li = older(li, 18)
for i in li:
    i.info()
