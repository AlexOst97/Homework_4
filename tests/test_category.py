from src.category import Category
from src.product import Product


def test_category_1():
    category1 = Category("Одежда", "Виды одежды", [])
    product1 = Product("Футболка", "Футболка размера-Х", 500, 10)
    category1.add_product(product1)
    assert category1.name == "Одежда"
    assert category1.description == "Виды одежды"
    assert category1.products == "Футболка, 500 руб. Остаток: 10 шт.\n"
    assert category1.number_categories == 1
    assert category1.number_products == 1

    product2 = Product("Джинсы", "Джинсы синие", 1000, 5)
    category1.add_product(product2)
    assert category1.products == "Футболка, 500 руб. Остаток: 10 шт.\nДжинсы, 1000 руб. Остаток: 5 шт.\n"
    assert category1.number_categories == 1
    assert category1.number_products == 2

    category2 = Category("Продукты", "Мясные изделия", ["Колбаса", "Сосиски", "Сало"])
    assert category2.number_categories == 2
    assert category2.number_products == 5
