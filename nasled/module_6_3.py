class Horse:
    def __init__(self, x_distance = 0, y_distance = 0, sound = 'Frrr'):
        self._x_distance = x_distance
        self.sound = sound
        super().__init__(y_distance)

    def run(self, dx):
        self._x_distance += dx
        print(self._x_distance)
        
class Eagle:
    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self._y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self._y_distance += dy
        print(self._y_distance)

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        pass

    def move(self, dx, dy):
        super().__init__(dx, dy)
        # super().run
        # super().fly

    def get_pos(self):
        Tuple_ = (self._x_distance, self._y_distance)
        return Tuple_

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
