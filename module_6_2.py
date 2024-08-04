class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self, __model):
        self.__model = __model
        return f'Модель: {__model}'

    def get_color(self, __color):
        self.__color = __color
        return f'Цвет: {__color}'

    def get_horsepower(self, __engine_power):
        self.__engine_power = __engine_power
        return f"Мощность двигателя: {__engine_power}"

    def print_info(self):
        print(self.get_model(self.__model))
        print(self.get_horsepower(self.__engine_power))
        print(self.get_color(self.__color))
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color


        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
