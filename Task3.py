class Cell:
    quantity: int

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        c1 = Cell
        c1.quantity = self.quantity + other.quantity
        return c1

    def __sub__(self, other):
        c1 = Cell
        c1.quantity = self.quantity - other.quantity
        if c1.quantity <= 0:
            print("Нет клеток")
            return None
        else:
            return c1

    def __mul__(self, other):
        c1 = Cell
        c1.quantity = self.quantity * other.quantity
        return c1

    def __truediv__(self, other):
        c1 = Cell
        c1.quantity = round(self.quantity / other.quantity)
        return c1

    def make_order(self, row_quantity):
        i = 0
        s = -1
        l = str()
        while s < self.quantity:
            i += 1
            s += 1
            l = l + '*'
            if i == row_quantity:
                i = 0
                l = l + "\n"
        return l


a = Cell(30)
b = Cell(5)
print(f'a: {a.quantity} b: {b.quantity}')
print(f'/: {(a / b).quantity}')
print(f'*: {(a * b).quantity}')
print(f'+: {(a + b).quantity}')
print(f'-: {(a - b).quantity}')
n = 4
print(f'{a.quantity} клеток в группы по {n}')
print(a.make_order(n))
