import pytest

from src.category import Category


@pytest.fixture()
def category_1():
    return Category("Продукты", "Мясные изделия", ["Колбаса", "Сосиски", "Сало"])


@pytest.fixture()
def category_2():
    return Category("Автозапчасти", "Шины", ["Летние", "Зимние", "Всесезонные"])


def test_category_2(category_1, category_2):
    assert category_1.name == "Продукты"
    assert category_1.description == "Мясные изделия"
    assert category_1.products == ["Колбаса", "Сосиски", "Сало"]
    assert category_2.name == "Автозапчасти"
    assert category_2.description == "Шины"
    assert category_2.products == ["Летние", "Зимние", "Всесезонные"]
    assert category_2.number_categories == 2
    assert category_2.number_products == 6
