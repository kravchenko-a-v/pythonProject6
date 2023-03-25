class Person:
    def __init__(self, name, lastname, age):
        self.__name = name
        self.__lastname = lastname
        self.__age = age

    def info(self):
        print(f'name = {self.__name}, age = {self.__age}, '
              f'lastname = {self.__lastname}')


# f = open('dz.txt', 'w')
f = open('dz.txt', 'r')
a = f.readlines()
li = []
for i in a:
    i = i[:-1]
    b = i.split(' ')
    person = Person(b[0], b[1], b[2])
    li.append(person)
for i in li:
    i.info()
