from src.product import Product


def test_product_initialization():
    """
    Тест корректности инициализации товара
    """
    product = Product("Ноутбук", "Мощный игровой", 150000.0, 10)

    assert product.name == "Ноутбук"
    assert product.description == "Мощный игровой"
    assert product.price == 150000.0
    assert product.quantity == 10
