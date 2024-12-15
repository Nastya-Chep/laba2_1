# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Book:
    """
     Создание объекта "Книга"

        :param name: Название книги
        :param count_pages: Общее количество страниц
        :param pages_now: Количество прочитанных страниц

        Пример:
        >>> book1 = Book("Война и мир", 500, 30)
    """
    def __init__(self, name: str, count_pages: int, pages_now: int):
        if not isinstance(name, str):
            raise TypeError("Не соответствует тип данных")
        self.name = name

        if not isinstance(count_pages, int):
            raise TypeError("Не соответствует тип данных")
        if count_pages <= 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        self.count_pages = count_pages

        if not isinstance(pages_now, int):
            raise TypeError("Не соответствует тип данных")
        if pages_now < 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        self.pages_now = pages_now

    def read_book(self, pages: int) -> None:
        """
         Функция, которая добавляет количество прочитанных страниц

        :param pages: Количество прочитанных страниц
        :raise TypeError: Если не соответствует тип данных, то вызывается ошибка
        :raise ValueError: Если количество страниц отрицательное, то вызывается ошибка
        :raise ValueError: Если количество страниц превышает общее количество страниц, то вызывается ошибка

        Пример:
        >>> book1 = Book("Война и мир", 500, 30)
        >>> book1.read_book(155)
        """
        if not isinstance(pages, int):
            raise TypeError("Не соответствует тип данных")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        if (self.pages_now + pages) > self.count_pages:
            raise ValueError("Превышает количество допустимых страниц")
        ...

    def searching_name(self, search_name: str) -> bool:
        """
        Функция, проверяет книгу по названию

        :param search_name: Название искомой книги
        :return: Совпадает ли название книги с искомым названием
        :raise TypeError: Если не соответствует тип данных, то вызывается ошибка

        Пример:
        >>> book1 = Book("Война и мир", 500, 30)
        >>> book1.searching_name("Отцы и дети")
        """
        if not isinstance(search_name, str):
            raise TypeError("Не соответствует тип данных")
        ...


class Table:
    """
     Создание объекта "Стол"

        :param width: Ширина стола
        :param length: Длина стола

        Пример:
        >>> table1 = Table(60, 90)
    """
    def __init__(self, width: int, length: int):
        if not isinstance(width, int):
            raise TypeError("Не соответствует тип данных")
        if width <= 0:
            raise ValueError("Ширина стола не может быть отрицательным")
        self.width = width

        if not isinstance(length, int):
            raise TypeError("Не соответствует тип данных")
        if length <= 0:
            raise ValueError("Длина стола не может быть отрицательным")
        self.length = length

    def area_of_table(self) -> int:
        """
         Функция, которая считает площадь стола

         :return: Площадь стола

        Пример:
        >>> table1 = Table(60, 90)
        >>> table1.area_of_table()
        """
        ...

    def perimeter_of_table(self) -> int:
        """
        Функция, которая считает периметр стола

        :return: Периметр стола

        Пример:
        >>> table1 = Table(60, 90)
        >>> table1.perimeter_of_table()
        """
        ...


class SchoolJournal:
    """
     Создание объекта "Школьный журнал"

        :param subject: Школьный предмет
        :param number_of_five: Количество пятёрок
        :param number_of_two: Количество двоек

        Пример:
        >>> journal = SchoolJournal("Математика", 10, 3)
    """

    def __init__(self, subject: str, number_of_five: int, number_of_two: int):
        if not isinstance(subject, str):
            raise TypeError("Не соответствует тип данных")
        self.subject = subject

        if not isinstance(number_of_five, int):
            raise TypeError("Не соответствует тип данных")
        if number_of_five < 0:
            raise ValueError("Количество оценок не может быть отрицательным")
        self.number_of_five = number_of_five

        if not isinstance(number_of_two, int):
            raise TypeError("Не соответствует тип данных")
        if number_of_two < 0:
            raise ValueError("Количество оценок не может быть отрицательным")
        self.number_of_two = number_of_two

    def add_fives(self, count: int) -> None:
        """
         Функция, которая увеличивает количество пятерок в журнале

        :param count: Количество добавленной оценки
        :raise TypeError: Если не соответствует тип данных, то вызывается ошибка
        :raise ValueError: Если количество оценок отрицательное, то вызывается ошибка

        Пример:
        >>> journal = SchoolJournal("Математика", 10, 3)
        >>> journal.add_fives(2)
        """
        if not isinstance(count, int):
            raise TypeError("Не соответствует тип данных")
        if count < 0:
            raise ValueError("Количество оценок не может быть отрицательным")
        ...

    def average_score(self) -> float:
        """
        Функция, которая считает средний балл оценок

        :return: Средний балл

        Пример:
        >>> journal = SchoolJournal("Математика", 10, 3)
        >>> journal.average_score()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
