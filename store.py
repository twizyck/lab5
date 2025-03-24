# Базовый класс для товаров
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name}, Цена: {self.price} руб."


# Разные категории товаров
class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def get_info(self):
        return f"Электроника: {self.name}, Бренд: {self.brand}, Цена: {self.price} руб."


class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_info(self):
        return f"Одежда: {self.name}, Размер: {self.size}, Цена: {self.price} руб."


class Shoes(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def get_info(self):
        return f"Обувь: {self.name}, Бренд: {self.brand}, Цена: {self.price} руб."


# Класс пользователя с балансом и корзиной
class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cart = []
        self.history = []

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product.name} добавлен в корзину.")

    def checkout(self):
        total = sum(item.price for item in self.cart)
        if total > self.balance:
            print("Недостаточно средств!")
        else:
            confirmation = input("Подтвердите покупку (да/нет): ").strip().lower()
            if confirmation == "да":
                self.balance -= total
                self.history.extend(self.cart)
                self.cart.clear()
                print("Покупка успешно завершена!")
            else:
                print("Покупка отменена.")

    def show_balance(self):
        print(f"Ваш баланс: {self.balance} руб.")

    def add_funds(self, amount):
        self.balance += amount
        print(f"Баланс пополнен на {amount} руб.")


# Главное меню
if __name__ == "__main__":
    user = User("Алексей", 5000)
    products = [
        Electronics("Смартфон", 3000, "Samsung"),
        Clothing("Футболка Adidas", 1200, "M"),
        Clothing("Футболка Nike", 1400, "L"),
        Clothing("Футболка Puma", 1300, "XL"),
        Shoes("Кроссовки Reebok", 5000, "Reebok"),
        Shoes("Кроссовки Nike", 6000, "Nike"),
        Shoes("Кроссовки Adidas", 5500, "Adidas"),
        Clothing("Шорты Puma", 2000, "L")
    ]

    while True:
        print("\n1. Посмотреть товары\n2. Корзина\n3. Баланс\n4. Пополнить счет\n5. История покупок\n6. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            for i, product in enumerate(products, 1):
                print(f"{i}. {product.get_info()}")
            prod_choice = int(input("Выберите товар: ")) - 1
            user.add_to_cart(products[prod_choice])
        elif choice == "2":
            if user.cart:
                for item in user.cart:
                    print(item.get_info())
                user.checkout()
            else:
                print("Корзина пуста.")
        elif choice == "3":
            user.show_balance()
        elif choice == "4":
            amount = int(input("Введите сумму пополнения: "))
            user.add_funds(amount)
        elif choice == "5":
            for item in user.history:
                print(item.get_info())
        elif choice == "6":
            break