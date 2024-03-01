// Laba3 V2.0.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//
﻿#include <iostream>
#include <vector>

namespace Data { // объявление пространства имён
    template<typename T> // шаблон
    class Array3d {
    private:
        int dim0;
        int dim1;
        int dim2;
        std::vector<T> data;

    public:

        Array3d(int dim0, int dim1, int dim2) : dim0(dim0), dim1(dim1), dim2(dim2) { // Здесь используется список инициализации членов для инициализации 
            //членов dim0, dim1, dim2 класса Array3d значениями, переданными в конструктор
            data.resize(dim0 * dim1 * dim2);
        }


        T& operator()(int i, int j, int k) {
            return data[i * dim1 * dim2 + j * dim2 + k];
        }


        std::vector<T> GetValues0(int i) {
            std::vector<T> slice(dim1 * dim2);
            for (int j = 0; j < dim1; j++) {
                for (int k = 0; k < dim2; k++) {
                    slice[j * dim2 + k] = data[i * dim1 * dim2 + j * dim2 + k];
                }
            }
            return slice;
        }


        std::vector<T> GetValues1(int j) {
            std::vector<T> slice(dim0 * dim2);
            for (int i = 0; i < dim0; i++) {
                for (int k = 0; k < dim2; k++) {
                    slice[i * dim2 + k] = data[i * dim1 * dim2 + j * dim2 + k];
                }
            }
            return slice;
        }


        std::vector<T> GetValues2(int k) {
            std::vector<T> slice(dim0 * dim1);
            for (int i = 0; i < dim0; i++) {
                for (int j = 0; j < dim1; j++) {
                    slice[i * dim1 + j] = data[i * dim1 * dim2 + j * dim2 + k];
                }
            }
            return slice;
        }


        std::vector<T> GetValues01(int i, int j) {
            std::vector<T> slice(dim2);
            for (int k = 0; k < dim2; k++) {
                slice[k] = data[i * dim1 * dim2 + j * dim2 + k];
            }
            return slice;
        }


        std::vector<T> GetValues02(int i, int k) {
            std::vector<T> slice(dim1);
            for (int j = 0; j < dim1; j++) {
                slice[j] = data[i * dim1 * dim2 + j * dim2 + k];
            }
            return slice;
        }


        std::vector<T> GetValues12(int j, int k) {
            std::vector<T> slice(dim0);
            for (int i = 0; i < dim0; i++) {
                slice[i] = data[i * dim1 * dim2 + j * dim2 + k];
            }
            return slice;
        }


        void SetValues0(int i, std::vector<std::vector<T>> values) {
            for (int j = 0; j < dim1; j++) {
                for (int k = 0; k < dim2; k++) {
                    data[i * dim1 * dim2 + j * dim2 + k] = values[j][k];
                }
            }
        }

        void SetValues1(int j, std::vector<std::vector<T>> values) {
            for (int i = 0; i < dim0; i++) {
                for (int k = 0; k < dim2; k++) {
                    data[i * dim1 * dim2 + j * dim2 + k] = values[i][k];
                }
            }
        }


        void SetValues2(int k, std::vector<std::vector<T>> values) {
            for (int i = 0; i < dim0; i++) {
                for (int j = 0; j < dim1; j++) {
                    data[i * dim1 * dim2 + j * dim2 + k] = values[i][j];
                }
            }
        }


        void SetValues01(int i, int j, std::vector<T> values) {
            for (int k = 0; k < dim2; k++) {
                data[i * dim1 * dim2 + j * dim2 + k] = values[k];
            }
        }


        void SetValues02(int i, int k, std::vector<T> values) {
            for (int j = 0; j < dim1; j++) {
                data[i * dim1 * dim2 + j * dim2 + k] = values[j];
            }
        }


        void SetValues12(int j, int k, std::vector<T> values) {
            for (int i = 0; i < dim0; i++) {
                data[i * dim1 * dim2 + j * dim2 + k] = values[i];
            }
        }


        void ones() {
            for (int i = 0; i < dim0; i++) {
                for (int j = 0; j < dim1; j++) {
                    for (int k = 0; k < dim2; k++) {
                        data[i * dim1 * dim2 + j * dim2 + k] = 1;
                    }
                }
            }
        }

        void zeros() {
            for (int i = 0; i < dim0; i++) {
                for (int j = 0; j < dim1; j++) {
                    for (int k = 0; k < dim2; k++) {
                        data[i * dim1 * dim2 + j * dim2 + k] = 0;
                    }
                }
            }
        }

        void fill(T value) {
            for (int i = 0; i < dim0; i++) {
                for (int j = 0; j < dim1; j++) {
                    for (int k = 0; k < dim2; k++) {
                        data[i * dim1 * dim2 + j * dim2 + k] = value;
                    }
                }
            }
        }


        void arrayPrint() {
            for (int i = 0; i < dim0; i++) {
                std::cout << "i = " << i << std::endl;
                for (int j = 0; j < dim1; j++) {
                    for (int k = 0; k < dim2; k++) {
                        std::cout << data[i * dim1 * dim2 + j * dim2 + k] << " ";
                    }
                    std::cout << std::endl;
                }
                std::cout << std::endl;
            }
        }
    };
}

int main() {
    Data::Array3d<int> arr(2, 3, 4);

    arr.SetValues0(0, { {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12} });
    arr.arrayPrint();
    std::vector<int> slice = arr.GetValues0(0);
    for (int i : slice) {
        std::cout << i << " ";
    }
    std::cout << "\n""\n";
    arr.SetValues1(1, { {13, 14, 15, 16}, {17, 18, 19, 20}, {21, 22, 23, 24} });
    arr.arrayPrint();
    slice = arr.GetValues1(1);
    for (int i : slice) {
        std::cout << i << " ";
    }
    std::cout << "\n""\n";
    arr.SetValues2(0, { {25, 26, 27, 28}, {29, 30, 31, 32}, {33, 34, 35, 36} });
    arr.arrayPrint();
    slice = arr.GetValues2(2);
    for (int i : slice) {
        std::cout << i << " ";
    }
    std::cout << "\n""\n";
    arr.SetValues01(0, 1, { {37, 38, 39, 40} });
    arr.arrayPrint();
    slice = arr.GetValues01(0, 1);
    for (int i : slice) {
        std::cout << i << " ";
    }
    std::cout << "\n""\n";
    arr.SetValues02(0, 2, { {41, 42, 43, 44} });
    arr.arrayPrint();
    slice = arr.GetValues02(0, 2);
    for (int i : slice) {
        std::cout << i << " ";
    }
    std::cout << "\n""\n";
    arr.SetValues12(1, 2, { {45, 46, 47, 48} });
    arr.arrayPrint();
    slice = arr.GetValues12(0, 2);
    for (int i : slice) {
        std::cout << i << " ";
    }
    std::cout << "\n""\n";
    arr.zeros();
    arr.arrayPrint();
    arr.ones();
    arr.arrayPrint();
    arr.fill(500);
    arr.arrayPrint();

    return 0;
}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
