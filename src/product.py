from abc import ABC, abstractmethod


class BaseProduct(ABC):
    '''Абстрактный класс'''

    @abstractmethod
    def __add__(self, other):
        pass


class MixinProduct:
    '''Класс-миксин'''
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})'


class Product(BaseProduct, MixinProduct):
    """Класс, описывающий продукты"""

    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if self.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            sum_goods = (self.__price * self.quantity) + (other.__price * other.quantity)
            return sum_goods
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product):
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Smartphone(Product):
    """Класс, Смартфон"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # производительность
        self.model = model  # модель
        self.memory = memory  # объем встроенной памяти
        self.color = color  # цвет

    def __add__(self, other):
        if type(other) is Smartphone:
            sum_goods = (self.price * self.quantity) + (other.price * other.quantity)
            return sum_goods
        else:
            raise TypeError


class LawnGrass(Product):
    """Класс, Трава газонная"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country  # страна-производитель
        self.germination_period = germination_period  # срок прорастания
        self.color = color  # цвет

    def __add__(self, other):
        if type(other) is LawnGrass:
            sum_goods = (self.price * self.quantity) + (other.price * other.quantity)
            return sum_goods
        else:
            raise TypeError


# if __name__ == "__main__":
#     print('КЛАСС Product')
#     product1 = Product("Молоко", "Тогучинское", 66.6, 47)
#     product2 = Product("Масло", "Сливочное", 200.0, 15)
#     print(product1)
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#
#     print('КЛАСС Smartphone')
#     product3 = Smartphone("Телефоны", "Cмартфоны", 97700, 7, "Apple", "iPhone 14 Pro Max", "256 ГБ", "Золотой")
#     product4 = Smartphone("Телефоны", "Cмартфоны", 127700, 12, "Apple", "iPhone 15 Pro Max", "256 ГБ", "Золотой")
#     print(product3.name)
#     print(product3.description)
#     print(product3.price)
#     print(product3.quantity)
#     print(product3.efficiency)
#     print(product3.model)
#     print(product3.memory)
#     print(product3.color)
#     print(product3+product4)
#
#
#     print('КЛАСС LawnGrass')
#     product5 = LawnGrass("Покрытие для спорта", "Для футбола", 156000, 55, "Россия", "5 суток", "Зеленая")
#     product6 = LawnGrass("Покрытие для спорта", "Для футбола", 106500, 74, "Россия", "5 суток", "Зеленая")
#     print(product5.name)
#     print(product5.description)
#     print(product5.price)
#     print(product5.quantity)
#     print(product5.country)
#     print(product5.germination_period)
#     print(product5.color)
#     print(product5 + product6)
#
#
#     product7 = Product("Молоко", "Тогучинское", 66.6, 0)
#     print(product7)

