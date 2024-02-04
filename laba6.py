# Базовый класс для всех контролов
class Control:
    def setPosition(self, x, y):
        print(f"Вызван метод setPosition у контролла {self.__class__.__name__} с параметрами x={x}, y={y}")

    def getPosition(self):
        print(f"Вызван метод getPosition у контролла {self.__class__.__name__}")

# Класс для формы, содержащей контроллы
class Form(Control):
    def __init__(self):
        self.controls = []

    def addControl(self, control):
        self.controls.append(control)
        print(f"Вызван метод addControl у формы. Добавлен контролл {control.__class__.__name__}")

# Класс для метки
class Label(Control):
    def setText(self, text):
        print(f"Вызван метод setText у метки. Установлен текст: {text}")

    def getText(self):
        print(f"Вызван метод getText у метки")

# Класс для текстового поля
class TextBox(Control):
    def setText(self, text):
        print(f"Вызван метод setText у текстового поля. Установлен текст: {text}")

    def getText(self):
        print(f"Вызван метод getText у текстового поля")

    def onValueChanged(self):
        print(f"Вызван метод onValueChanged у текстового поля")

# Класс для комбо-бокса
class ComboBox(Control):
    def getSelectedIndex(self):
        print(f"Вызван метод getSelectedIndex у комбо-бокса")

    def setSelectedIndex(self, index):
        print(f"Вызван метод setSelectedIndex у комбо-бокса. Установлен индекс: {index}")

    def setItems(self, items):
        print(f"Вызван метод setItems у комбо-бокса. Установлены элементы: {items}")

    def getItems(self):
        print(f"Вызван метод getItems у комбо-бокса")

# Класс для кнопки
class Button(Control):
    def setText(self, text):
        print(f"Вызван метод setText у кнопки. Установлен текст: {text}")

    def getText(self):
        print(f"Вызван метод getText у кнопки")

    def click(self):
        print(f"Вызван метод click у кнопки")

# Создание фабрик для различных операционных систем
class ControlFactory:
    def createForm(self):
        pass

    def createLabel(self):
        pass

    def createTextBox(self):
        pass

    def createComboBox(self):
        pass

    def createButton(self):
        pass

# Фабрика для Windows
class WindowsControlFactory(ControlFactory):
    def createForm(self):
        return WindowsForm()

    def createLabel(self):
        return WindowsLabel()

    def createTextBox(self):
        return WindowsTextBox()

    def createComboBox(self):
        return WindowsComboBox()

    def createButton(self):
        return WindowsButton()

# Фабрика для Linux
class LinuxControlFactory(ControlFactory):
    def createForm(self):
        return LinuxForm()

    def createLabel(self):
        return LinuxLabel()

    def createTextBox(self):
        return LinuxTextBox()

    def createComboBox(self):
        return LinuxComboBox()

    def createButton(self):
        return LinuxButton()

# Фабрика для MacOS
class MacOSControlFactory(ControlFactory):
    def createForm(self):
        return MacOSForm()

    def createLabel(self):
        return MacOSLabel()

    def createTextBox(self):
        return MacOSTextBox()

    def createComboBox(self):
        return MacOSComboBox()

    def createButton(self):
        return MacOSButton()

# Классы для конкретных контролов и форм для Windows
class WindowsForm(Form):
    pass

class WindowsLabel(Label):
    pass

class WindowsTextBox(TextBox):
    pass

class WindowsComboBox(ComboBox):
    pass

class WindowsButton(Button):
    pass

# Классы для конкретных контролов и форм для Linux
class LinuxForm(Form):
    pass

class LinuxLabel(Label):
    pass

class LinuxTextBox(TextBox):
    pass

class LinuxComboBox(ComboBox):
    pass

class LinuxButton(Button):
    pass

# Классы для конкретных контролов и форм для MacOS
class MacOSForm(Form):
    pass

class MacOSLabel(Label):
    pass

class MacOSTextBox(TextBox):
    pass

class MacOSComboBox(ComboBox):
    pass

class MacOSButton(Button):
    pass

# Пример использования
def run_simulation(factory):
    form = factory.createForm()
    label = factory.createLabel()
    textBox = factory.createTextBox()
    comboBox = factory.createComboBox()
    button = factory.createButton()

    form.addControl(label)
    form.addControl(textBox)
    form.addControl(comboBox)
    form.addControl(button)

    label.setText("Привет, мир!")
    textBox.setText("Текстовое поле")
    comboBox.setItems(["Опция 1", "Опция 2", "Опция 3"])
    button.click()

# Выбор фабрики в зависимости от операционной системы
os_name = "Windows"  # Замените на свою текущую операционную систему
if os_name == "Windows":
    factory = WindowsControlFactory()
elif os_name == "Linux":
    factory = LinuxControlFactory()
elif os_name == "MacOS":
    factory = MacOSControlFactory()
else:
    raise ValueError("Неизвестная операционная система")

run_simulation(factory)
