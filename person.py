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
            self.__name = age
        else:
            self.__age = 0

ivan = Person('Ivan', 'Ivanov', 25)
petr = Person('Petr', 'Petrov', 29)
ivan.info()
ivan.set_age('123fwe')