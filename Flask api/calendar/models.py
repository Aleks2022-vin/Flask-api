# Определяем класс Event для представления события
class Event:
    def __init__(self, id, date, title, text):
        self.id = id  # Уникальный идентификатор события
        self.date = date  # Дата события
        self.title = title  # Заголовок события
        self.text = text  # Текст события

    # Метод для строкового представления события
    def __repr__(self):
        return f"Event({self.id}, {self.date}, {self.title}, {self.text})"