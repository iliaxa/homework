class House:

    houses_history = []
        
    def __new__(cls, *args, **kwargs):
        cls.args = args 
        cls.kwargs = kwargs
        cls.houses_history.append(cls.args[0])
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.quantity_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.quantity_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor):
                print(f"Идём на {i} этаж")
            print(f"Пришли на {new_floor} этаж")

    def __len__(self):
        return self.quantity_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.quantity_floors == other.quantity_floors
        elif isinstance(other, int):
            return self.quantity_floors == other
        else:
            return f"UNSUPPORTED TYPE"

    def __lt__(self, other):
        if isinstance(other, House):
            return self.quantity_floors < other.quantity_floors
        elif isinstance(other, int):
            return self.quantity_floors < other
        else:
            return f"UNSUPPORTED TYPE"

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if isinstance(other, House):
            self.quantity_floors += other.quantity_floors
        elif isinstance(other, int):
            self.quantity_floors += other
        else:
            return f"UNSUPPORTED TYPE"
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other:int):
        return self.__add__(other)

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.quantity_floors}"

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)
