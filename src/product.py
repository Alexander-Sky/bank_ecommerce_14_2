class Product:
    """Класс для представления товара."""

    name: str
    description: str
    __price: float  # приватный атрибут
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация товара
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для цены с проверкой.
        Доп. задание: при понижении цены запрашиваем подтверждение.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Доп. задание: проверка на понижение цены
        if new_price < self.__price:
            answer = input(f"Цена понижается с {self.__price} до {new_price}. Подтвердите (y/n): ")
            if answer.lower() != 'y':
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list = None) -> 'Product':
        """
        Класс-метод для создания продукта из словаря.
        Доп. задание: проверка дубликатов по имени.
        """
        # Доп. задание: проверка на дубликаты
        if existing_products is not None:
            for existing in existing_products:
                if existing.name.lower() == product_data["name"].lower():
                    # Складываем количество
                    existing.quantity += product_data["quantity"]
                    # Берём максимальную цену
                    if product_data["price"] > existing.price:
                        existing.price = product_data["price"]
                    return existing

        # Если дубликата нет — создаём новый продукт
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )