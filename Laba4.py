import os
from pynput import keyboard
from colorama import Fore, Back, Style, init
import time

init(autoreset=True)

class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class Workflow:
    def __init__(self):
        self.commands = []  # Инициализация списка команд

    def add_command(self, command):
        self.commands.append(command)  # Добавление команды в список

    def execute(self):
        for command in self.commands:
            command.execute()  # Выполнение всех команд из списка

    def undo(self):
        if self.commands:
            command = self.commands.pop()
            command.undo()  # Отмена последней команды

class Key:
    def __init__(self, key_combination):
        self.assign_command = None
        self.key_combination = key_combination

    def press(self, key_combination):
        if self.assign_command and key_combination == self.key_combination:
            self.assign_command.execute()  # Выполнение назначенной команды при нажатии клавиши

    def assign(self, command):
        self.assign_command = command  # Назначение команды клавише

class Keyboard:
    def __init__(self):
        self.keys = []  # Инициализация списка клавиш
        self.press_stack = []  # Инициализация стека нажатий клавиш

    def add_key(self, key):
        self.keys.append(key)  # Добавление клавиши в список

    def press_key(self, key_combination):
        for key in self.keys:
            key.press(key_combination)  # Вызов метода press для каждой клавиши
            self.press_stack.append(key)  # Добавление клавиши в стек нажатий

    def undo(self):
        if self.press_stack:
            key = self.press_stack.pop()
            key.assign_command.undo()  # Отмена последнего нажатия клавиши и выполнение отмены команды

class KeyboardListener:
    def __init__(self, keyboard_manager):
        self.keyboard_manager = keyboard_manager
        self.alt_pressed = False
        self.current_key = None
        self.listener = keyboard.Listener(on_press=self._on_key_press, on_release=self._on_key_release)
        self.listener.start()  # Инициализация мониторинга клавиатуры

    def _on_key_press(self, key):
        try:
            self.current_key = key.char
        except AttributeError:
            self.current_key = str(key)

        if key == keyboard.Key.alt_l:
            self.alt_pressed = True  # Установка флага при нажатии левой клавиши Alt

        self.keyboard_manager.press_key(self.current_key)  # Вызов метода press_key при нажатии клавиши

    def _on_key_release(self, key):
        if key == keyboard.Key.alt_l:
            self.alt_pressed = False  # Сброс флага при отпускании левой клавиши Alt

        if key == keyboard.KeyCode.from_char('a') and self.alt_pressed:
            # Очистка последнего действия при нажатии Alt + a
            os.system('cls' if os.name == 'nt' else 'clear')

            # Отмена последней команды
            self.keyboard_manager.undo()

        self.current_key = None

class PrintCommand(Command):
    def __init__(self, message, color=Fore.WHITE):
        self.message = message
        self.color = color

    def execute(self):
        print(f"{self.color}{self.message}{Fore.RESET}")  # Вывод сообщения с цветом в консоль

    def undo(self):
        print(f"\r{' ' * len(self.message)}\r{Fore.BLACK + Back.WHITE}Undo: {self.message}{Style.RESET_ALL}", end='')  # Вывод отмены команды в консоль

# Создаем экземпляры классов
workflow = Workflow()  # Создание объекта Workflow
keyboard_manager = Keyboard()  # Создание объекта Keyboard
keyboard_listener = KeyboardListener(keyboard_manager)  # Создание объекта KeyboardListener с передачей объекта Keyboard

key_a = Key('a')  # Создание объекта Key для клавиши 'a'
key_b = Key('b')  # Создание объекта Key для клавиши 'b'

command_1 = PrintCommand("Action 1", Fore.GREEN)  # Создание объекта PrintCommand с сообщением и зеленым цветом
command_2 = PrintCommand("Action 2", Fore.BLUE)  # Создание объекта PrintCommand с сообщением и синим цветом

# Привязываем команды к клавишам
key_a.assign(command_1)
key_b.assign(command_2)

# Добавляем клавиши в клавиатуру
keyboard_manager.add_key(key_a)
keyboard_manager.add_key(key_b)

# Добавляем команды в Workflow
workflow.add_command(command_1)
workflow.add_command(command_2)

# Демонстрация работы клавиатуры
keyboard_manager.press_key('a')
keyboard_manager.press_key('b')

# Демонстрация отката
workflow.undo()

# Демонстрация переназначения клавиши
key_a.assign(command_2)

# Повторная демонстрация работы клавиатуры с новым назначением
keyboard_manager.press_key('a')

# Задержка, чтобы вы могли увидеть результат перед завершением программы
time.sleep(200)
