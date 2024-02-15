class Category:
    '''
    класс категория хранит название категории,
      описание категории,
      список входящих продуктов
    '''
    name: str
    description: str
    products: list
    count_name = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.count_name += 1
        self.count_products = len(self.products)


class Product:
    '''
    класс продукт хранит название продукта,
    описание продукта
    стоимость продукта
    количество продукта
    '''
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
