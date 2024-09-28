from models import Event

# Хранилище для событий
events = {}

# Функция для получения всех событий
def get_events():
    return list(events.values())  # Возвращаем список всех событий

# Функция для получения события по его ID
def get_event(event_id):
    return events.get(event_id)  # Возвращаем событие по ID, если оно существует

# Функция для создания нового события
def create_event(date, title, text):
    # Проверяем длину заголовка и текста
    if len(title) > 30 or len(text) > 200:
        raise ValueError("Максимальная длина заголовка - 30 символов, максимальная длина поля Текст - 200 символов")
    # Проверяем, существует ли уже событие на эту дату
    if date in events:
        raise ValueError("Нельзя добавить больше одного события в день")
    # Генерируем новый ID для события
    event_id = len(events) + 1
    # Создаем новое событие и добавляем его в хранилище
    events[event_id] = Event(event_id, date, title, text)
    return event_id  # Возвращаем ID нового события

# Функция для обновления существующего события
def update_event(event_id, date, title, text):
    # Проверяем, существует ли событие с данным ID
    if event_id not in events:
        raise ValueError("Событие не найдено")
    # Проверяем длину заголовка и текста
    if len(title) > 30 or len(text) > 200:
        raise ValueError("Максимальная длина заголовка - 30 символов, максимальная длина поля Текст - 200 символов")
    # Обновляем данные события
    events[event_id].date = date
    events[event_id].title = title
    events[event_id].text = text

# Функция для удаления события по его ID
def delete_event(event_id):
    # Проверяем, существует ли событие с данным ID
    if event_id not in events:
        raise ValueError("Событие не найдено")
    # Удаляем событие из хранилища
    del events[event_id]