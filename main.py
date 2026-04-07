from src.category import Category
from src.product import Product

if __name__ == "__main__":

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Проверка геттера
    print("=== Товары в категории Смартфоны ===")
    print(category1.products)

    # Проверка add_product
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры", "Современный телевизор", [product4])

    print("\n=== Товары в категории Телевизоры ===")
    print(category2.products)

    # Проверка сеттера цены
    print("\n=== Проверка изменения цены ===")
    print(f"Старая цена: {product1.price}")
    product1.price = 170000.0  # понижение — запросит подтверждение
    print(f"Новая цена: {product1.price}")

    # Проверка new_product
    print("\n=== Проверка new_product ===")
    existing_products = [product1, product2, product3]
    new_phone = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB", "price": 190000.0, "quantity": 3},
        existing_products=existing_products
    )
    print(f"Товар: {new_phone.name}, цена: {new_phone.price}, количество: {new_phone.quantity}")

    print(f"\nВсего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
