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
        self.products = products
        Category.number_categories += 1
        Category.number_products += len(products)


# if __name__ == '__main__':
#     xxx1 = Category("Продукты", "Мясные изделия", ["Колбаса", "Сосиски", "Сало"])
#     print(xxx1.number_categories)
#     print(xxx1.number_products)
#     xxx2 = Category("Автозапчасти", "Шины", ["Летние", "Зимние", "Всесезонные"])
#     print(xxx2.number_categories)
#     print(xxx2.number_products)
