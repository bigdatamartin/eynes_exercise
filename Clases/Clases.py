import math

class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor a 0.")
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, value):
        if value <= 0:
            raise ValueError("El radio debe ser mayor a 0.")
        self._radio = value

    def area(self):
        return math.pi * self._radio ** 2

    def perimetro(self):
        return 2 * math.pi * self._radio

    def __str__(self):
        return f"Circulo de radio {self._radio}"

    def __repr__(self):
        return f"Circulo({self._radio})"

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("El multiplicador debe ser mayor a 0.")
        return Circulo(self._radio * n)
