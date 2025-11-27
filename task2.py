from abc import abstractmethod, ABC


class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_all_books(self) -> list[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book) -> None:
        self.books.append(book)

    def remove_book(self, title) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def get_all_books(self) -> list[Book]:
        return self.books


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        print(f"Book '{title}' was successfully added")

    def remove_book(self, title) -> None:
        self.library.remove_book(title)
        print(f"Book '{title}' was successfully removed")

    def show_books(self) -> None:
        books = self.library.get_all_books()
        if not books:
            print("There are no books in the library")
        else:
            for book in books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            manager.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
