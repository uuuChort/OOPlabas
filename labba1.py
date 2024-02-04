
class NumericalIntegration:
    def __init__(self, num_points, step, precision):
        self.num_points = num_points
        self.step = step
        self.precision = precision

    def calc(self, func, lower_bound, upper_bound):
        """
        Метод для численного расчета интеграла.

        :param func: Подынтегральное выражение в виде функции.
        :param lower_bound: Нижняя граница интегрирования.
        :param upper_bound: Верхняя граница интегрирования.
        :return: Значение интеграла.
        """
        # Проверка на корректность переданных параметров
        if not callable(func):
            raise ValueError("Подынтегральное выражение должно быть функцией.")

        # Дополнительные проверки на корректность границ интегрирования, числа точек и шага

        # Заглушка для базового класса
        raise NotImplementedError("Метод calc не реализован в базовом классе.")


class TrapezoidalIntegration(NumericalIntegration):
    def calc(self, func, lower_bound, upper_bound):
        # Реализация метода трапеций для расчета интеграла
        result = 0.5 * (func(lower_bound) + func(upper_bound)) * (upper_bound - lower_bound)
        return result


class SimpsonIntegration(NumericalIntegration):
    def calc(self, func, lower_bound, upper_bound):
        # Реализация метода Симпсона для расчета интеграла
        h = (upper_bound - lower_bound) / self.num_points
        result = (h / 3) * (func(lower_bound) + func(upper_bound) +
                            4 * sum(func(lower_bound + i * h) for i in range(1, self.num_points, 2)) +
                            2 * sum(func(lower_bound + i * h) for i in range(2, self.num_points - 1, 2)))
        return result


def example_function(x):
    return x ** 2


# Аналитическое значение интеграла для функции x^2 на интервале от 0 до 1
analytical_result = 1 / 3

# Пример использования класса для метода трапеций
trap_integration = TrapezoidalIntegration(num_points=100, step=None, precision=None)
result_trap = trap_integration.calc(example_function, 0, 1)
print(f"Метод трапеций: {result_trap}, Аналитическое: {analytical_result}")

# Пример использования класса для метода Симпсона
simp_integration = SimpsonIntegration(num_points=100, step=None, precision=None)
result_simp = simp_integration.calc(example_function, 0, 1)
print(f"Метод Симпсона: {result_simp}, Аналитическое: {analytical_result}")