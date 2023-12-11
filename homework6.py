# Dmitry Atroshchenko
# Description: Homework 6
# Date: 11/12/2023
# My version Python 3.11

# Программа по бронированию номеров в отеле в которой мы через классовое представления добавили атрибуты номеров
# клиентов и самого отеля и вней обыгрывается ситуация бронирования номера сначала первым клментом "Alice" и повторной
# попыткой бронирования того же номера но уже другим человеком "Bob" чтобы получить результат
# что этот номер уже забронирован

# Определение класса Room (комната в отеле)
class Room:
    def __init__(self, room_number, capacity, price_per_night):
        # Инициализация атрибутов комнаты
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        # Флаг, указывающий, забронирована ли комната
        self.is_booked = False
        # Гость, забронировавший комнату
        self.guest = None

    # Метод для бронирования комнаты
    def book_room(self, guest):
        # Проверка, не забронирована ли уже комната
        if not self.is_booked:
            self.is_booked = True
            self.guest = guest
            print(f"Room {self.room_number} booked by {guest.name}.")
        else:
            print(f"Room {self.room_number} is already booked.")

# Определение класса Guest (гость)
class Guest:
    def __init__(self, name, age):
        # Инициализация атрибутов гостя
        self.name = name
        self.age = age

# Определение класса Hotel (отель)
class Hotel:
    def __init__(self, name):
        # Инициализация атрибутов отеля
        self.name = name
        self.rooms = []  # Список комнат в отеле

    # Метод для добавления комнаты в отель
    def add_room(self, room):
        self.rooms.append(room)
        print(f"Room {room.room_number} added to {self.name}.")

# Создание отеля и нескольких комнат
hotel = Hotel("Luxury Hotel")
room1 = Room(101, 2, 150)
room2 = Room(102, 4, 250)
room3 = Room(103, 1, 100)

# Добавление комнат в отель
hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

# Создание гостей
guest1 = Guest("Alice", 25)
guest2 = Guest("Bob", 30)

# Бронирование комнаты гостем
room1.book_room(guest1)

# Попытка повторного бронирования комнаты
room1.book_room(guest2)


# Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без исключений
# (но не более n раз - параметр декоратора). Если превышено количество попыток, должно быть возбуждено
# исключение типа TooManyErrors

# Определение пользовательского исключения для случая превышения максимального числа попыток
class TooManyErrors(Exception):
    pass

# Определение декоратора с параметром max_attempts
def retry(max_attempts):
    # Внутренний декоратор, который принимает функцию для декорирования
    def decorator(func):
        # Объявление внутренней функции-обертки
        def wrapper(*args, **kwargs):
            # Инициализация счетчика попыток
            attempts = 0
            # Запуск цикла, который продолжается до достижения максимального числа попыток
            while attempts < max_attempts:
                try:
                    # Вызов декорированной функции
                    result = func(*args, **kwargs)
                    # Возврат результата в случае успешного выполнения
                    return result
                except Exception as e:
                    # Обработка исключения: вывод информации о неудачной попытке и увеличение счетчика
                    print(f"Attempt {attempts + 1} failed with error: {str(e)}")
                    attempts += 1
            # Если достигнуто максимальное число попыток, возбуждение пользовательского исключения
            raise TooManyErrors(f"Exceeded maximum number of attempts ({max_attempts})")

        # Возврат функции-обертки из декоратора
        return wrapper
    # Возврат внутреннего декоратора из основного декоратора
    return decorator

# Пример использования декоратора
@retry(max_attempts=3)
def example_function():
    # Импорт модуля random для генерации случайных чисел
    import random
    # Генерация случайного числа 0 или 1
    if random.randint(0, 1) == 0:
        # Вывод сообщения об успешном выполнении функции
        print("Function succeeded")
    else:
        # Если случайное число равно 1, возбуждение исключения ValueError для имитации неудачной попытки
        raise ValueError("Function failed")

# Попытка вызова декорированной функции, обработка возможного исключения TooManyErrors
try:
    example_function()
except TooManyErrors as e:
    # Вывод информации об исключении в случае превышения максимального числа попыток
    print(f"Caught TooManyErrors: {str(e)}")
