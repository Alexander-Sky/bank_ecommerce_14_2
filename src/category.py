from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса (общие для всех объектов)
    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """
        Инициализация категории
        """
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счётчик категорий при создании нового объекта
        Category.category_count += 1

        # Увеличиваем общий счётчик товаров на количество товаров в этой категории
        Category.product_count += len(self.products)
