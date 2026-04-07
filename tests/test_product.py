import pytest
from src.product import Product


def test_product_initialization():
    """Тест корректности инициализации товара"""
    product = Product("Ноутбук", "Мощный игровой", 150000.0, 10)

    assert product.name == "Ноутбук"
    assert product.description == "Мощный игровой"
    assert product.price == 150000.0
    assert product.quantity == 10


def test_product_price_getter():
    """Тест геттера цены"""
    product = Product("Телефон", "Смартфон", 50000.0, 5)
    assert product.price == 50000.0


def test_product_price_setter_positive():
    """Тест сеттера цены с положительным значением"""
    product = Product("Телефон", "Смартфон", 50000.0, 5)
    product.price = 60000.0
    assert product.price == 60000.0


def test_product_price_setter_zero_or_negative(capsys):
    """Тест сеттера цены с неположительным значением"""
    product = Product("Телефон", "Смартфон", 50000.0, 5)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 50000.0  # цена не изменилась

    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 50000.0


def test_new_product_no_duplicate():
    """Тест new_product без дубликатов"""
    product = Product.new_product({
        "name": "Планшет",
        "description": "10 дюймов",
        "price": 25000.0,
        "quantity": 3
    })
    assert product.name == "Планшет"
    assert product.price == 25000.0
    assert product.quantity == 3


def test_new_product_with_duplicate():
    """Тест new_product с дубликатом (доп. задание)"""
    existing = Product("Ноутбук", "Игровой", 80000.0, 2)

    result = Product.new_product(
        {"name": "Ноутбук", "description": "Игровой", "price": 90000.0, "quantity": 3},
        existing_products=[existing]
    )

    # Должен вернуть существующий объект
    assert result is existing
    # Количество сложилось
    assert existing.quantity == 5
    # Цена взята максимальная
    assert existing.price == 90000.0
