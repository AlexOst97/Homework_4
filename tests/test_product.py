import pytest

from src.product import Product


@pytest.fixture()
def product_1():
    return Product("Молоко", "Тогучинское", 66.6, 47)


@pytest.fixture()
def product_2():
    return Product("Масло", "Сливочное", 200.0, 15)


def test_product_1(product_1):
    assert product_1.name == "Молоко"
    assert product_1.description == "Тогучинское"
    assert product_1.price == 66.6
    assert product_1.quantity == 47


def test_product_2(product_1):
    product_1.price = 77.7
    assert product_1.price == 77.7


def test_product_3(product_1):
    product_1.price = -77.7
    assert product_1.price == 66.6


def test_product_4(product_1, product_2):
    assert product_1 + product_2 == 6130.2
