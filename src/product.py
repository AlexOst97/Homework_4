class Product:
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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product) or issubclass(type(other), Product):
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
        if isinstance(other, Smartphone) or issubclass(type(other), Smartphone):
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
        if isinstance(other, LawnGrass) or issubclass(type(other), LawnGrass):
            sum_goods = (self.price * self.quantity) + (other.price * other.quantity)
            return sum_goods
        else:
            raise TypeError


if __name__ == "__main__":
    # product1 = Smartphone("Телефоны", "Cмартфоны", 97700, 7, "Apple", "iPhone 14 Pro Max", "256 ГБ", "Золотой")
    # product2 = Smartphone("Телефоны", "Cмартфоны", 127700, 12, "Apple", "iPhone 15 Pro Max", "256 ГБ", "Золотой")
    # print(product1.name)
    # print(product1.description)
    # print(product1.price)
    # print(product1.quantity)
    # print(product1.efficiency)
    # print(product1.model)
    # print(product1.memory)
    # print(product1.color)
    # print(product1+product2)

    product3 = LawnGrass("Покрытие для спорта", "Для футбола", 156000, 55, "Россия", "5 суток", "Зеленая")
    product4 = LawnGrass("Покрытие для спорта", "Для футбола", 106500, 74, "Россия", "5 суток", "Зеленая")
    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)
    print(product3.country)
    print(product3.germination_period)
    print(product3.color)
    print(product3 + product4)
