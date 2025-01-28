import pytest

from src.product import LawnGrass, Product, Smartphone


@pytest.fixture()
def product_1():
    return Product("Молоко", "Тогучинское", 66.6, 47)


@pytest.fixture()
def product_2():
    return Product("Масло", "Сливочное", 200.0, 15)


@pytest.fixture()
def product_smartphone_1():
    return Smartphone("Телефоны", "Cмартфоны", 97700, 7, "Apple", "iPhone 14 Pro Max", "256 ГБ", "Золотой")


@pytest.fixture()
def product_smartphone_2():
    return Smartphone("Телефоны", "Cмартфоны", 127700, 12, "Apple", "iPhone 15 Pro Max", "256 ГБ", "Золотой")


@pytest.fixture()
def product_lawngrass_1():
    return LawnGrass("Покрытие для спорта", "Для футбола", 156000, 55, "Россия", "5 суток", "Зеленая")


@pytest.fixture()
def product_lawngrass_2():
    return LawnGrass("Покрытие для спорта", "Для футбола", 106500, 74, "Россия", "5 суток", "Зеленая")


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


def test_product_5(product_smartphone_1, product_smartphone_2):
    assert product_smartphone_1.name == "Телефоны"
    assert product_smartphone_1.description == "Cмартфоны"
    assert product_smartphone_1.price == 97700
    assert product_smartphone_1.quantity == 7
    assert product_smartphone_1.efficiency == "Apple"
    assert product_smartphone_1.model == "iPhone 14 Pro Max"
    assert product_smartphone_1.memory == "256 ГБ"
    assert product_smartphone_1.color == "Золотой"

    assert product_smartphone_2.name == "Телефоны"
    assert product_smartphone_2.description == "Cмартфоны"
    assert product_smartphone_2.price == 127700
    assert product_smartphone_2.quantity == 12
    assert product_smartphone_2.efficiency == "Apple"
    assert product_smartphone_2.model == "iPhone 15 Pro Max"
    assert product_smartphone_2.memory == "256 ГБ"
    assert product_smartphone_2.color == "Золотой"

    assert product_smartphone_1 + product_smartphone_2 == 2216300

    with pytest.raises(TypeError):
        product_smartphone_1 + 1


def test_product_6(product_lawngrass_1, product_lawngrass_2):
    assert product_lawngrass_1.name == "Покрытие для спорта"
    assert product_lawngrass_1.description == "Для футбола"
    assert product_lawngrass_1.price == 156000
    assert product_lawngrass_1.quantity == 55
    assert product_lawngrass_1.country == "Россия"
    assert product_lawngrass_1.germination_period == "5 суток"
    assert product_lawngrass_1.color == "Зеленая"

    assert product_lawngrass_2.name == "Покрытие для спорта"
    assert product_lawngrass_2.description == "Для футбола"
    assert product_lawngrass_2.price == 106500
    assert product_lawngrass_2.quantity == 74
    assert product_lawngrass_2.country == "Россия"
    assert product_lawngrass_2.germination_period == "5 суток"
    assert product_lawngrass_2.color == "Зеленая"

    assert product_lawngrass_1 + product_lawngrass_2 == 16461000

    with pytest.raises(TypeError):
        product_lawngrass_1 + 1


def test_product_7(capsys):
    Product("Молоко", "Тогучинское", 66.6, 47)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(Молоко, Тогучинское, 66.6, 47)'


def test_product_8(capsys):
    Smartphone("Телефоны", "Cмартфоны", 97700, 7, "Apple", "iPhone 14 Pro Max", "256 ГБ", "Золотой")
    message = capsys.readouterr()
    assert message.out.strip() == 'Smartphone(Телефоны, Cмартфоны, 97700, 7)'


def test_product_9(capsys):
    LawnGrass("Покрытие для спорта", "Для футбола", 156000, 55, "Россия", "5 суток", "Зеленая")
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass(Покрытие для спорта, Для футбола, 156000, 55)'