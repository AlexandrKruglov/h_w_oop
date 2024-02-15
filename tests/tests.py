import pytest

import my_class


@pytest.fixture
def exmp_1():
    return my_class.Category('tv', 'look tv', ['rubin', 'lg'])


@pytest.fixture
def exmp_2():
    return my_class.Product('lg', 'good tv', 5.5, 6)


def test_init_category(exmp_1):
    assert exmp_1.name == 'tv'
    assert exmp_1.description == 'look tv'
    assert exmp_1.products == ['rubin', 'lg']
    assert exmp_1.count_name == 1
    assert exmp_1.count_products == 2
def test_init_product(exmp_2):
    assert exmp_2.name == 'lg'
    assert exmp_2.description == 'good tv'
    assert exmp_2.price == 5.5
    assert exmp_2.quantity == 6

