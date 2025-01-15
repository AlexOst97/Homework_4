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
        sum_goods = (self.__price * self.quantity) + (other.__price * other.quantity)
        return sum_goods

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


# if __name__ == '__main__':
#     product1 = Product("Молоко", "Тогучинское", 66.6, 47)
#     product2 = Product("Масло", "Сливочное", 200.0, 15)
#     print(product1)
#     print(product2)
#     print(product1 + product2)
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#     product1.price = -77.7
