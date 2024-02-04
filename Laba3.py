class Array3d:
    def __init__(self, dim0, dim1, dim2):
        # Инициализация размеров массива и самого массива данными
        self.dim0 = dim0
        self.dim1 = dim1
        self.dim2 = dim2
        self.data = [0] * (dim0 * dim1 * dim2)

    def __getitem__(self, index):
        # Перегрузка оператора [] для доступа к элементам массива
        i, j, k = index
        return self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k]

    def __setitem__(self, index, value):
        # Перегрузка оператора [] для установки значения элемента массива
        i, j, k = index
        self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = value

    # Методы для получения срезов данных по разным осям
    def get_values_0(self, i):
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for j in range(self.dim1) for k in range(self.dim2)]

    def get_values_1(self, j):
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for i in range(self.dim0) for k in range(self.dim2)]

    def get_values_2(self, k):
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for i in range(self.dim0) for j in range(self.dim1)]

    # Методы для получения срезов данных по плоскостям
    def get_values_01(self, i, j):
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for k in range(self.dim2)]

    def get_values_02(self, i, k):
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for j in range(self.dim1)]

    def get_values_12(self, j, k):
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for i in range(self.dim0)]

    # Методы для установки срезов данных по разным осям
    def set_values_0(self, i, values):
        for j in range(self.dim1):
            for k in range(self.dim2):
                self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[j][k]

    def set_values_1(self, j, values):
        for i in range(self.dim0):
            for k in range(self.dim2):
                self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[i][k]

    def set_values_2(self, k, values):
        for i in range(self.dim0):
            for j in range(self.dim1):
                self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[i][j]

    # Методы для установки срезов данных по плоскостям
    def set_values_01(self, i, j, values):
        for k in range(self.dim2):
            self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[k]

    def set_values_02(self, i, k, values):
        for j in range(self.dim1):
            self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[j]

    def set_values_12(self, j, k, values):
        for i in range(self.dim0):
            self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[i]

    # Методы для установки единиц, нулей или заполнения массива значением
    def ones(self):
        self.data = [1] * (self.dim0 * self.dim1 * self.dim2)

    def zeros(self):
        self.data = [0] * (self.dim0 * self.dim1 * self.dim2)

    def fill(self, value):
        self.data = [value] * (self.dim0 * self.dim1 * self.dim2)

    # Метод для вывода массива в консоль
    def array_print(self):
        for i in range(self.dim0):
            print(f"i = {i}")
            for j in range(self.dim1):
                for k in range(self.dim2):
                    print(self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k], end=" ")
                print()
            print()


# Пример использования
arr = Array3d(2, 3, 4)

arr.set_values_0(0, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
arr.set_values_0(1, [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]])

arr.array_print()

slice = arr.get_values_0(1)

for i in slice:
    print(i, end=" ")
print()
