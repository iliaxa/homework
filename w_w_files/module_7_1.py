from pprint import pprint

class Product:
    """
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.
"""
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
        

# class Shop:
    
    
#     def __init__(self):
#         file_name = 'products.txt'

#     def get_products(self):
#         product_list = ''
#         open(file_name, 'r')
#         print(file_name.read())
    
#         file_name.close()
