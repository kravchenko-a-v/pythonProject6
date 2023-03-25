class Auto:
    def __init__(self, model, color):
        self.__model = model
        self.__color = color

    def ifo(self):
        print(f'model = {self.__model}, color = {self.__color}')

    def set_col(self,__color):
        print(__color)


bmw = Auto(3,'red')
audi = Auto('A5', 'grin')
bmw.set_col('black')
audi.ifo()

