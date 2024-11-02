import sqlite3


def create_database():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            year INTEGER
        )
    ''')
    connection.commit()
    connection.close()


def add_book(title, author, year):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO books (title, author, year) VALUES (?, ?, ?)
    ''', (title, author, year))
    connection.commit()
    connection.close()


def add_sample_books():
    add_book('1984', 'George Orwell', 1949)
    add_book('To Kill a Mockingbird', 'Harper Lee', 1960)
    add_book('The Great Gatsby', 'F. Scott Fitzgerald', 1925)


def find_book_by_title(title):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books WHERE title = ?', (title,))
    book = cursor.fetchone()
    connection.close()
    return book


def update_book_year(title, new_year):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE books SET year = ? WHERE title = ?
    ''', (new_year, title))
    connection.commit()
    connection.close()


def delete_book_by_title(title):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE title = ?', (title,))
    connection.commit()
    connection.close()


def menu():
    create_database()
    add_sample_books()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Искать книгу по названию")
        print("3. Обновить год издания книги")
        print("4. Удалить книгу по названию")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            add_book(title, author, year)
            print("Книга добавлена.")
        
        elif choice == '2':
            title = input("Введите название книги для поиска: ")
            book = find_book_by_title(title)
            if book:
                print(f"Найдена книга: {book}")
            else:
                print("Книга не найдена.")
        
        elif choice == '3':
            title = input("Введите название книги для обновления года: ")
            new_year = int(input("Введите новый год издания: "))
            update_book_year(title, new_year)
            print("Год издания обновлен.")
        
        elif choice == '4':
            title = input("Введите название книги для удаления: ")
            delete_book_by_title(title)
            print("Книга удалена.")
        
        elif choice == '5':
            print("Выход из программы.")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    menu()
