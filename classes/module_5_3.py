class House:

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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1.name)
print(h1.quantity_floors)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__                                                                         
