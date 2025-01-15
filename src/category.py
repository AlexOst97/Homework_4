from src.product import Product


class Category:
    """Класс, описывающий категории"""

    name: str  # название
    description: str  # описание
    products: list  # список товаров категории
    number_categories = 0  # количество категорий
    number_products = 0  # количество товаров

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.number_categories += 1
        Category.number_products += len(products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.number_products} шт."

    def add_product(self, new_products: Product):
        self.__products.append(new_products)
        Category.number_products += 1

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str


if __name__ == "__main__":
    category1 = Category("Одежда", "Виды одежды", [])

    # product1 = Product("Футболка", "Футболка размера-Х", 500, 10)
    # product2 = Product("Джинсы", "Джинсы синие", 1000, 5)
    # category1.add_product(product1)
    # category1.add_product(product2)
    # print(category1)
#     print(category1.name)
#     print(category1.description)
#     print(category1.products)
#     print(category1.number_categories)
#     print(category1.number_products)
#
#     category2 = Category("Продукты", "Мясные изделия", ["Колбаса", "Сосиски", "Сало"])
#     print(category2.number_categories)
#     print(category2.number_products)
