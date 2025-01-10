import pytest

from src.product import Product


@pytest.fixture()
def product_1():
    return Product("Молоко", "Тогучинское", "66.6", "47")


def test_product_1(product_1):
    assert product_1.name == "Молоко"
    assert product_1.description == "Тогучинское"
    assert product_1.price == "66.6"
    assert product_1.quantity == "47"
