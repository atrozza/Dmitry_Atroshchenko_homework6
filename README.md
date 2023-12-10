#### Dmitry Atroshchenko
#### Description: Homework 6
#### Date: 10/12/2023
#### My version Python 3.11


  
# **Система бронирования номеров в отеле**
Этот репозиторий содержит простую программу на Python для бронирования номеров в отеле. Программа использует классы для представления номеров отеля, гостей и самого отеля. В ней демонстрируется процесс бронирования номера, а также обрабатывается ситуация, когда номер уже забронирован.

### **Описание**
Программа моделирует систему бронирования номеров в отеле. В ней определены три класса:
1. `Room` **(Комната)**: Представляет номер отеля с атрибутами, такими как номер комнаты, вместимость, стоимость за ночь, статус бронирования и информация о госте.
2. `Guest` **(Гость)**: Представляет гостя с атрибутами, такими как имя и возраст.
3. `Hotel` **(Отель)**: Представляет сам отель, содержащий список комнат и методы для добавления комнат.

### **Классы**
#### **Room (Комната)**
##### **Атрибуты:**
- `room_number`: Номер комнаты.
- `capacity`: Максимальная вместимость комнаты.
- `price_per_night`: Стоимость проживания за ночь.
- `is_booked`: Булево значение, указывающее, забронирована ли комната.
- `guest`: Ссылка на гостя, забронировавшего комнату.  
##### **Методы:**
- `book_room(guest)`: Забронировать комнату для указанного гостя, если комната еще не забронирована.

#### **Guest (Гость)**
##### **Атрибуты:**
- `name`: Имя гостя.
- `age`: Возраст гостя.

#### **Hotel (Отель)**
##### **Атрибуты:**
- `name`: Название отеля.
- `rooms`: Список комнат в отеле.  
##### **Методы:**
- `add_room(room)`: Добавить комнату в отель.
