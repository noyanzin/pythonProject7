class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        a = list()
        for i in range(len(self.matrix)):
            b = list()
            for j in range(len(self.matrix[i])):
                b.append(self.matrix[i][j] + other.matrix[i][j])
            a.append(b)
        return a


b = [[10, 20, 30], [40, 50, 60]]
a = [[1, 2, 3], [4, 5, 6]]
m1 = Matrix(a)
m2 = Matrix(b)
print(m1 + m2)
