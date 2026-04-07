from src.category import Category
from src.product import Product


def test_category_initialization():
    """
    Тест корректности инициализации категории
    """
    product1 = Product("Телефон", "Смартфон", 50000.0, 5)
    product2 = Product("Чехол", "Силиконовый", 1000.0, 20)
    products_list = [product1, product2]

    category = Category("Электроника", "Разные гаджеты", products_list)

    assert category.name == "Электроника"
    assert category.description == "Разные гаджеты"
    assert len(category.products) == 2
    assert category.products[0].name == "Телефон"
    assert category.products[1].name == "Чехол"


def test_category_counters():
    """
    Тест подсчета количества категорий и товаров
    """
    # Обнуляем счетчики перед тестом (на случай, если другие тесты их меняли)
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Ноутбук", "Мощный", 80000.0, 3)
    product2 = Product("Мышь", "Беспроводная", 2000.0, 15)
    category1 = Category("Компьютеры", "Техника", [product1, product2])
    assert category1.name == "Компьютеры"

    product3 = Product("Футболка", "Хлопок", 1500.0, 10)
    category2 = Category("Одежда", "Мужская", [product3])
    assert category2.name == "Одежда"
