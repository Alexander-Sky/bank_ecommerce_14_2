import pytest
from src.category import Category
from src.product import Product


def test_category_initialization():
    """Тест корректности инициализации категории"""
    product1 = Product("Телефон", "Смартфон", 50000.0, 5)
    product2 = Product("Чехол", "Силиконовый", 1000.0, 20)
    products_list = [product1, product2]

    category = Category("Электроника", "Разные гаджеты", products_list)

    assert category.name == "Электроника"
    assert category.description == "Разные гаджеты"
    # Через геттер проверяем (раньше был прямой доступ к products)
    assert "Телефон" in category.products
    assert "Чехол" in category.products


def test_category_counters():
    """Тест подсчета количества категорий и товаров"""
    # Обнуляем счетчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Ноутбук", "Мощный", 80000.0, 3)
    product2 = Product("Мышь", "Беспроводная", 2000.0, 15)
    category1 = Category("Компьютеры", "Техника", [product1, product2])

    product3 = Product("Футболка", "Хлопок", 1500.0, 10)
    category2 = Category("Одежда", "Мужская", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3  # 2 + 1 товар


def test_add_product():
    """Тест метода add_product"""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Ноутбук", "Мощный", 80000.0, 3)
    category = Category("Компьютеры", "Техника", [])

    assert Category.product_count == 0

    category.add_product(product1)

    assert "Ноутбук" in category.products
    assert Category.product_count == 1


def test_products_property_format():
    """Тест формата вывода геттера products"""
    product1 = Product("Смартфон", "Новый", 50000.0, 10)
    category = Category("Гаджеты", "Разное", [product1])

    expected = "Смартфон, 50000.0 руб. Остаток: 10 шт."
    assert category.products == expected