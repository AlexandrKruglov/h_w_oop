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
        self.__products = products
        self.count_name += 1
        self.count_products = len(self.__products)

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f'{self.name}, Количество товаров: {len(self)}'

    def get_list_podukts(self):
        '''
        :return:список продуктов
        '''
        return self.__products

    def add_obj(self, obj_prod):
        '''
         добавляент продукт в список продуктов
        :param obj_prod:принимоет объект класса продукт
        '''
        self.__products.append(obj_prod)


    @property
    def input_info(self):
        '''
        выводит список проуктов категории в нужном формате
        '''
        list_products = self.__products
        new_list = []
        for i in list_products:
            new_list.append(str(i))
        return "\n".join(new_list)


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

    def __str__(self):
        return (f'{self.name}, {self.price}руб. Остаток: {self.quantity}шт.')

    @classmethod
    def create_product(cls, dict_prod):
        '''
        создает объект класса продукт из словаря
        :param dict_prod: словарь
        :return: объект клааса продукт
        '''
        new_obj_prod = cls(dict_prod["name"], dict_prod["description"], dict_prod["price"], dict_prod["quantity"])
        return new_obj_prod

    @property
    def chek_price(self):
        '''
       возвращает цену продукта
        '''
        return self.price

    @chek_price.setter
    def chek_price(self, new_price):
        '''
        изменяет цену продукта
        :param new_price: новая цена
        :return: если новая цена = 0 или < 0 возвращает "некоректная цена"
        в противном случае меняет цену
        '''
        if new_price <= 0:
            print("некоректная цена")
        self.price = new_price

    def __add__(self, other):
        '''
        складывает общуюсумму стоимость всех единиц двух видов продукта
        '''
        return self.price * self.quantity + other.price * other.quantity


class RangeProductc:
    '''
    который  дает возможность использовать цикл for
    для прохода по всем товарам данной категории.
    при запросе
    for i in RangeProductc(len(Сategory)):
    print(i)
    '''

    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        self.value = -1
        return self

    def __next__(self):
        if self.value + 1 < self.stop:
            self.value += 1
            return self.value
        else:
            raise StopIteration
