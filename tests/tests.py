import pytest

from src.my_class import Category, Product


@pytest.fixture
def exmp_1():
    return Category('tv', 'look tv', [exmp_2])


@pytest.fixture
def exmp_2():
    return Product('lg', 'good tv', 5.5, 6)

@pytest.fixture
def exmp_3():
    return Product('sony', 'bed tv', 2, 10)


def tests_init_category(exmp_1):
    assert exmp_1.name == 'tv'
    assert exmp_1.description == 'look tv'
    assert exmp_1.count_name == 1
    assert exmp_1.count_products == 1


def tests_init_product(exmp_2):
    assert exmp_2.name == 'lg'
    assert exmp_2.description == 'good tv'
    assert exmp_2.price == 5.5
    assert exmp_2.quantity == 6


def tests_et_list_podukts(exmp_1):
    assert Category.get_list_podukts(exmp_1) == [exmp_2]


