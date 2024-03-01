// Laba1 V2.0.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

// Подключение необходимых библиотек
#include <iostream> // Библиотека для ввода/вывода
#include <functional>
#include <cmath>
#include <stdexcept> // Библиотека для обработки исключений

// Создание абстрактного класса IntegralCalculation
class IntegralCalculation {
public:
    // Конструктор класса с параметрами numPoints и step
    IntegralCalculation(int numPoints) {
        // Проверка на корректность параметров
        if (numPoints < 2)
            throw std::invalid_argument("Incorrect parameters"); // Генерация исключения с сообщением об ошибке
        else {
            this->numPoints = numPoints; // Присваивание значений numPoints и step
        }
    }

    // Виртуальный метод Calc, который будет переопределен в наследуемых классах
    virtual double Calc(const std::function<double(double)>& integralFunc, double lowerBound, double upperBound, double step) const = 0;

protected:
    int numPoints; // Количество точек
    double step; // Шаг интегрирования
};


// Создание класса Trapezoidal, наследующегося от IntegralCalculation
class Trapezoidal : public IntegralCalculation {
public:
    // Конструктор класса с параметрами numPoints и step, вызывающий конструктор базового класса
    Trapezoidal(int numPoints) : IntegralCalculation(numPoints) {}

    // Переопределение метода Calc
    double Calc(const std::function<double(double)>& integralFunc, double lowerBound, double upperBound, double step) const override {
        double result = 0.0; // Инициализация переменной result
        double x = lowerBound; // Присваивание x нижней границе интегрирования
        step = abs(lowerBound - upperBound) / numPoints;

        // Вычисление суммы функций * шага / 2
        for (int i = 0; i < numPoints; ++i) {
            double fx = integralFunc(x); // Вычисление значения функции integralFunc в точке x
            x += step; // Увеличение x на шаг
            result += fx; // Добавление значения функции к результату
        }
        result += (integralFunc(upperBound) - integralFunc(lowerBound)) / 2.0; // Добавление половины разности значений функции на верхней и нижней границах интегрирования
        result *= step; // Умножение результата на шаг

        return result; // Возвращение результата
    }
};

// Создание класса Simpson, наследующегося от IntegralCalculation
class Simpson : public IntegralCalculation {
public:
    // Конструктор класса с параметрами numPoints и step, вызывающий конструктор базового класса
    Simpson(int numPoints) : IntegralCalculation(numPoints) {
        if (numPoints % 2 != 0)
            throw std::invalid_argument("Incorrect parameters: the number of points must be a multiple of two");
    }

    // Переопределение метода Calc
    double Calc(const std::function<double(double)>& integralFunc, double lowerBound, double upperBound, double step) const override {
        double result = integralFunc(lowerBound) + integralFunc(upperBound); // Инициализация переменной result суммой значений функции на верхней и нижней границах интегрирования
        step = abs(lowerBound - upperBound) / numPoints;
        double x = lowerBound + step; // Присваивание x нижней границе интегрирования плюс шаг

        // Вычисление суммы f(x) + 2 * f(x + step) + 4 * f*(x + 2 * step) * step / 3
        for (int i = 1; i < numPoints; ++i) {
            double fx = integralFunc(x); // Вычисление значения функции integralFunc в точке x
            x += step; // Увеличение x на шаг

            if (i % 2 == 0)
                result += 2 * fx; // Если i четное, добавляем значение функции умноженное на 2 к результату
            else
                result += 4 * fx; // Если i нечетное, добавляем значение функции умноженное на 4 к результату
        }

        result *= step / 3.0; // Умножение результата на шаг и деление на 3

        return result; // Возвращение результата
    }
};

// Главная функция программы
int main() {
    try {
        int numPoints = 1000;// Количество точек
        double lowerBound = 0.0;// Нижняя граница интегрирования
        double upperBound = 1.0;// Верхняя граница интегрирования

        Trapezoidal trapezoidal(numPoints); // Создание объекта класса Trapezoidal с заданными параметрами
        auto integralFunc = [](double x) { return x * x; }; // Определение функции integralFunc, возвращающей значение x^2
        double integralResult = trapezoidal.Calc(integralFunc, lowerBound, upperBound, numPoints); // Вычисление интеграла методом трапеций
        std::cout << "Trapezoid method: " << integralResult << std::endl;// Вывод результата интеграла методом трапеций на экран

        Simpson simpson(numPoints); // Создание объекта класса Simpson с заданными параметрами
        integralResult = simpson.Calc(integralFunc, lowerBound, upperBound, numPoints); // Вычисление интеграла методом Симпсона
        std::cout << "Simpson's method: " << integralResult << std::endl;// Вывод результата интеграла методом Симпсона на экран
    }
    catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;// Вывод сообщения об ошибке на экран
    }

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
