# Завдання 3
# Створіть клас Book з атрибутами title (назва книги), author (автор) та genre (жанр). Додайте метод
# display_info, який виведе інформацію про книгу у вигляді "Назва: {title}, Автор: {author}, Жанр: {genre}".

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def print_info(self):
        print(f"Назва книги: {self.title}, Автор: {self.author}, Жанр: {self.genre}")

# Створення екземпляра класу
my_display_info = Book("Кобзар", "Т. Г. Шевченко", "вірші")
my_display_info.print_info()
