from abc import ABC, abstractmethod
# #
# # class ATM(ABC):
# #     @abstractmethod
# #     def insert_card(self):
# #         pass
# #
# # class BankATM(ATM):
# #     def insert_card(self): # Override qilishi shart!
# #         print(f"Insert card please")
# #
# #
# # a = BankATM()
# # a.insert_card()
#
#
# class Student:
#     count = 0
#     university = "INHA"
#
#     def __init__(self):
#         pass
#
#     @classmethod
#     def update_university(cls, university):
#         cls.university = university
#
#
# print(Student.university)


class LibraryItem(ABC):
    __total_items = 0

    def __init__(self, title, upc, subject):
        self.title = title
        self.upc = upc
        self.subject = subject
        LibraryItem.__total_items += 1

    @abstractmethod
    def locate(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, upc,  subject, isbn, dds_number):
        super().__init__(title=title, subject=subject, upc=upc)
        self.__isbn = isbn
        self.dds_number = dds_number
        self.authors = []

    def set_authors(self):
        pass

    def locate(self):
        pass


class DVD(LibraryItem):
    def __init__(self, title,  genre):
        super().__init__(title, upc=None, subject=None)
        self.genre = genre




