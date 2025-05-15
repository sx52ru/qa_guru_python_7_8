"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
import unittest

from homework.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity), f"Количество продукта {product.name} проходит проверку"
        # Непонятно почему именно проверки, а не одна проверка? Какие еще тут могут быть проверки?


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(product.quantity), f"Продукт {product.name} можно купить"
        # Аналогично.

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        pass
        # А вот тут вообще непонятно что нужно сделать (((
        #



class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """