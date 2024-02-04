import csv
from typing import List, Optional

# Определение класса пользователя
class User:
    def __init__(self, user_id: int, name: str, login: str, password: str):
        self.user_id = user_id
        self.name = name
        self.login = login
        self.password = password

# Определение базового интерфейса хранилища данных
class IDataRepository:
    def get(self, item_id: int) -> Optional:
        pass

    def add(self, item) -> int:
        pass

    def delete(self, item_id: int):
        pass

    def update(self, item):
        pass

# Интерфейс репозитория пользователей, расширяющий IDataRepository
class IUserRepository(IDataRepository):
    def find_by_id(self, user_id: int) -> Optional[User]:
        pass

    def find_by_name(self, name: str) -> Optional[User]:
        pass

# Класс репозитория пользователей, реализующий IUserRepository
class FileUserRepository(IUserRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.users: List[User] = []
        self.load_users_from_file()

    def load_users_from_file(self):
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    user_id, name, login, password = map(str.strip, row)
                    user = User(int(user_id), name, login, password)
                    self.users.append(user)
        except FileNotFoundError:
            pass

    def save_users_to_file(self):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            for user in self.users:
                writer.writerow([user.user_id, user.name, user.login, user.password])

    def find_by_id(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def find_by_name(self, name: str) -> Optional[User]:
        for user in self.users:
            if user.login == name:
                return user
        return None

    def get(self, user_id: int) -> Optional[User]:
        return self.find_by_id(user_id)

    def add(self, user: User) -> int:
        user_id = max([u.user_id for u in self.users] + [0]) + 1
        user.user_id = user_id
        self.users.append(user)
        self.save_users_to_file()
        return user_id

    def delete(self, user_id: int):
        self.users = [user for user in self.users if user.user_id != user_id]
        self.save_users_to_file()

    def update(self, user: User):
        existing_user = self.find_by_id(user.user_id)
        if existing_user:
            existing_user.name = user.name
            existing_user.login = user.login
            existing_user.password = user.password
            self.save_users_to_file()

# Интерфейс менеджера пользователей
class IUserManager:
    def login(self, login: str, password: str) -> Optional[User]:
        pass

    def logout(self):
        pass

    def is_authenticated(self) -> bool:
        pass

# Реализация менеджера пользователей, расширяющего IUserManager
class FileUserManager(IUserManager):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository
        self.current_user = None

    def login(self, login: str, password: str) -> Optional[User]:
        user = self.user_repository.find_by_name(login)
        if user and user.password == password:
            self.current_user = user
            return user
        else:
            return None

    def logout(self):
        self.current_user = None

    def is_authenticated(self) -> bool:
        return self.current_user is not None

# Точка входа в программу
if __name__ == "__main__":
    # Создаем репозиторий пользователей с файлом "users.csv"
    user_repository = FileUserRepository("users.csv")
    # Создаем менеджер пользователей, используя репозиторий
    user_manager = FileUserManager(user_repository)

    # Проверяем, авторизован ли пользователь
    if user_manager.is_authenticated():
        print(f"Logged in as {user_manager.current_user.name}")
    else:
        print("Not logged in. Please log in or register.")

        # Пользователю предоставляется выбор между входом и регистрацией
        choice = input("Enter '1' to login, '2' to register: ")
        if choice == '1':
            login = input("Enter your login: ")
            password = input("Enter your password: ")
            user = user_manager.login(login, password)
            if user:
                print(f"Successfully logged in as {user.name}")
            else:
                print("Login failed. Please check your credentials.")
        elif choice == '2':
            name = input("Enter your name: ")
            login = input("Choose a login: ")
            password = input("Choose a password: ")
            new_user = User(0, name, login, password)
            user_manager.user_repository.add(new_user)
            print(f"User {new_user.name} has been registered.")
        else:
            print("Invalid choice.")