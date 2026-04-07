from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса (общие для всех объектов)
    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    __products: list[Product]  # ПРИВАТНЫЙ атрибут

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """
        Инициализация категории
        """
        self.name = name
        self.description = description
        self.__products = products

        # Увеличиваем счётчик категорий при создании нового объекта
        Category.category_count += 1

        # Увеличиваем общий счётчик товаров на количество товаров в этой категории
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """
        Метод для добавления продукта в категорию.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер для вывода списка товаров в виде строки.
        Формат: "Название продукта, X руб. Остаток: X шт.\n"
        """
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result.rstrip("\n")  # убираем последний лишний перенос