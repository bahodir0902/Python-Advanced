class LibrarySystem:
    def __init__(self, Title, UPC, Subject):
        self.Title = Title
        self.UPC = UPC
        self.Subject = Subject

    def locate(self):
        pass


class Author:
    def __init__(self, author_name):
        self.author_name = author_name

    def get_author_name(self) -> str:
        return self.author_name

    def set_author_name(self, name: str) -> None:
        self.author_name = name


class Book(LibrarySystem):
    def __init__(self, ISBN, Authors: list[Author], Title, Subject, DDS_number, UPC):
        super().__init__(Title=Title, UPC=UPC, Subject=Subject)
        self.ISBN = ISBN
        self.Authors = Authors
        self.DDS_number = DDS_number

    def get_info(self) -> str:
        authors = [author.author_name for author in self.Authors]
        res = ", ".join(authors)
        return f"\n\t\tKitob ma\'lumotlari:\nKitob nomi: {self.Title} \nKitob ISBN: {self.ISBN} \nKitob mualliflari: {res} \nKitob DDS raqami: {self.DDS_number}, \nKitob UPC raqami: {self.UPC}, \nKitob janri: {self.Subject}"

    def set_book_title(self, title: str) -> None:
        self.Title = title

    def set_book_subject(self, subject: str) -> None:
        self.Subject = subject

    def set_book_ISBN(self, ISBN: str) -> None:
        self.ISBN = ISBN

    def set_book_upc(self, UPC: str) -> None:
        self.UPC = UPC

    def set_book_DSS_number(self, DDS_number: str) -> None:
        self.DDS_number = DDS_number

    def set_book_authors(self, authors: list[Author]) -> None:
        self.Authors = authors


class Magazine(LibrarySystem):
    def __init__(self, Volume: int, Issue: int):
        super().__init__(Title=None, UPC=None, Subject=None)
        self.Volume = Volume
        self.Issue = Issue

    def get_magazine_info(self) -> str:
        if not self.Issue and not self.Volume:
            return "Hech qanday jurnal ma\'lumotlari yo\'q!"
        else:
            return f"Jurnal hajmi: {self.Volume}, Jurnal chop etilgan yili: {self.Issue}"


class DVD(LibrarySystem):
    def __init__(self, Actors: list[str], Director, Genre):
        super().__init__(Title=None, UPC=None, Subject=None)
        self.Actors = Actors
        self.Director = Director
        self.Genre = Genre

    def get_dvd_info(self) -> str:
        if not self.Actors and not self.Director and not  self.Genre:
            return "Hech qanday DVD disk ma\'lumotlari yo\'q!"
        else:
            text = [actor for actor in self.Actors]
            res = ", ".join(text)
            return f"DVD aktyorlari: {res}, DVD Direktori: {self.Director}, DVD Janri: {self.Genre}"


class CD(LibrarySystem):
    def __init__(self, Artist: list[str]):
        super().__init__(Title=None, UPC=None, Subject=None)
        self.Artist = Artist

    def get_cd_info(self) -> str:
        if not self.Artist:
            return "Hech qanday CD disk ma\'lumotlari yo\'q!"
        else:
            text = [artist for artist in self.Artist]
            res = ", ".join(text)
            return f"CD artistlari: {res}"


class Catalog:
    def __init__(self):
        self.books = []
        self.cd_disks = []
        self.dvd_disks = []
        self.magazines = []

    def search_book(self, name="", author=""):
        try:
            if not name and not author:
                raise ValueError("Izlash uchun kiritilgan ma'lumotlar yo'q!")
        except ValueError as e:
            print(f"Xatolik! {e}")
            return
        for book in self.books:
            if (name and book.Title == name) or (author and book.Authors.author_name == author):
                print(f"Kitob topildi: {book.Title}, DDS: {book.DDS_number}")
                return
        print("Bunday kitob katalogda yo'q!")

    def add_book(self, book: Book) -> None:
        try:
            if not book or not isinstance(book, Book):
                raise TypeError("Kitob 'Book' turida bo'lishi kerak!")
        except TypeError as e:
            print(f"Xatolik! {e}")
            return

        self.books.append(book)
        print(f"{book.Title} nomli kitob katalogga qo'shildi.")

    def add_cd(self, cd: CD) -> None:
        try:
            if not cd or not isinstance(cd, CD):
                raise TypeError("CD 'CD' turida bo'lishi kerak!")
        except TypeError as e:
            print(f"Xatolik! {e}")
            return

        self.cd_disks.append(cd)
        print(f"{cd.Artist} nomli CD katalogga qo'shildi.")

    def add_dvd(self, dvd: DVD) -> None:
        try:
            if not dvd or not isinstance(dvd, DVD):
                raise TypeError("DVD 'DVD' turida bo'lishi kerak!")
        except TypeError as e:
            print(f"Xatolik! {e}")
            return

        self.dvd_disks.append(dvd)
        print(f"{dvd.Director} nomli DVD katalogga qo'shildi.")

    def add_magazine(self, magazine: Magazine) -> None:
        try:
            if not magazine or not isinstance(magazine, Magazine):
                raise TypeError("Jurnal 'Magazine' turida bo'lishi kerak!")
        except TypeError as e:
            print(f"Xatolik! {e}")
            return

        self.magazines.append(magazine)
        print(f"Jurnal katalogga qo'shildi. Volume: {magazine.Volume}, Issue: {magazine.Issue}")

    def get_catalog_info(self) -> str:
        text = f"\t\tKatalog ma\'lumotlari:\n"
        if self.books is None:
            text += f"Kitoblar: Kitoblar javoni bo\'m bo\'sh!\n"
        else:
            kitob = ""
            books = [book for book in self.books]
            for i, book in enumerate(books, 1):
                authors = [author.author_name for author in book.Authors]
                res = ", ".join(authors)
                kitob += f"{i}. Kitob nomi: {book.Title} \n  Kitob ISBN: {book.ISBN} \n  Kitob mualliflari: {res} \n  Kitob DDS raqami: {book.DDS_number}, \n  Kitob UPC raqami: {book.UPC}, \n  Kitob janri: {book.Subject}\n"
            text += f"{kitob}"
        text += "\t\tCD disk ma'lumotlari:\n"
        if not self.cd_disks:
            text += "CD disklar: CD disklar javoni bo'sh!\n"
        else:
            for i, disk in enumerate(self.cd_disks, 1):
                text += f"{i}. CD artistlari: {', '.join(disk.Artist)}\n"

        text += "\t\tDVD disk ma'lumotlari:\n"
        if not self.dvd_disks:
            text += "DVD disklar: DVD disklar javoni bo'sh!\n"
        else:
            for i, dvd in enumerate(self.dvd_disks, 1):
                actors = ", ".join(dvd.Actors)
                text += (f"{i}. DVD nomi: {dvd.Title} \n Aktyorlar: {actors} \n Rejissor: {dvd.Director} \n Janr: {dvd.Genre}\n")

        text += "\t\tJurnal ma'lumotlari:\n"
        if not self.magazines:
            text += "Jurnallar: Jurnallar javoni bo'sh!\n"
        else:
            for i, mag in enumerate(self.magazines, 1):
                text += (f"{i}. Jurnal nomi: {mag.Title} \n Hajmi: {mag.Volume} \n Noshir yili: {mag.Issue}\n")

        return text



catalog = Catalog()

author1 = Author("J.K. Rowling")
author2 = Author("George Orwell")

book1 = Book(ISBN="978-0747532743", Authors=[author1], Title="Harry Potter and the Philosopher's Stone", Subject="Fantasy", DDS_number="823.914", UPC="123456789")
book2 = Book(ISBN="978-0451524935", Authors=[author2], Title="1984", Subject="Dystopian", DDS_number="823.912", UPC="987654321")

catalog.add_book(book1)
catalog.add_book(book2)

#catalog.search_book(author="George Orwell")
# print(book1.get_info())
print(catalog.get_catalog_info())
