# --------დავალება 1(ValueError)--------
# class Celsius:
#
#     def __init__(self, temperature):
#         self.__temperature = temperature
#
#     def get_temperature(self):
#         return self.__temperature
#
#     def set_temperature(self, text):
#
#         if 0 <= text < 100:
#             self.__temperature = text
#         else:
#             raise ValueError("შეიტანეთ მნიშვნელობები 0-დან 100-მდე")
#
#
# obj1 = Celsius(25)
# print(obj1.get_temperature())
# obj1.set_temperature(10)
# print(obj1.get_temperature())


# --------დავალება 2(University)--------
# class People:
#
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#
#     def get_email(self):
#         return f"{self.first}.{self.last}.uni@btu.edu.ge"
#
#     def fullname(self):
#         return self.first + " " + self.last
#
#
# class Instructor(People):
#
#     def __init__(self, first, last, age, salary):
#         super().__init__(first, last, age)
#         self.__salary = salary
#
#     def get_salary(self):
#         return f"{self.__salary} ლარი"
#
#     def set_salary(self, text):
#         self.__salary = text
#
#     def get_email(self):
#         return f"{self.first}.{self.last}@btu.edu.ge"
#
#
# class Student(People):
#
#     def __init__(self, first, last, age, courses, grades):
#         super().__init__(first, last, age)
#         self.courses = courses
#         self.grades = grades
#
#     def get_average_grade(self):
#         return f"საშუალო ქულა = {sum(self.grades) / len(self.grades)}"
#
#     def get_email(self):
#         return f"{self.first}.{self.last}.1@btu.edu.ge"
#
#
# st1 = Student("Nika", "Kldiashvili", 18, ["Python", "კომპიუტერული ქსელები", "მათემატიკა", "მობილური აპლიკაციები"],
#               [86.3, 83, 94.5, 88])
# in1 = Instructor("Soso", "Ninidze", 25, 3000)
# print(st1.courses)
# print(st1.get_average_grade())
# print(st1.fullname())
# print(st1.get_email())
# print(in1.fullname())
# print(in1.get_email())
# print(in1.get_salary())


# --------დავალება 3(Library)--------
# class LibraryItem:
#     def __init__(self, title, subject, status):
#         self.title = title
#         self.subject = subject
#         self.status = status
#
#     def booking(self):
#         if self.status == "available":
#             print("Your item is available")
#             self.status = "occupied"
#         else:
#             print("Sorry, your item is not available")
#
#
# class Book(LibraryItem):
#     def __init__(self, isbn, authors, title, subject, status):
#         super().__init__(title, subject, status)
#         self.ISBN = isbn
#         self.authors = authors
#
#
# class Magazine(LibraryItem):
#     def __init__(self, journal_name, volume, status):
#         self.status = status
#         self.journalName = journal_name
#         self.volume = volume
#
#
# class CD(LibraryItem):
#     def __init__(self, title, status):
#         self.title = title
#         self.status = status
#
#     def booking(self):
#         print("Unfortunately, you cant reserve a CD in the library")
#
#
# b1 = Book(9781471331435, "George Orwell", "1984", "Romance", "available")
# m1 = Magazine("Nature", 580, "occupied")
# c1 = CD("Scorpion", "occupied")
#
# b1.booking()
# m1.booking()
# c1.booking()

# # --------დავალება 4(Contact Manager)--------
# class Contacts:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#
# class MailSender:
#     def send_mail(self):
#         return f"თქვენი მეილი გაიგზავნა ამ მისამართზე: {self.email}"
#
#
# class Friend(Contacts, MailSender):
#     def __init__(self, name, phone, email):
#         super().__init__(name, phone)
#         self.email = email
#
#
# class Family(Contacts, MailSender):
#     def __init__(self, name, phone, email, birth_date):
#         super().__init__(name, phone)
#         self.email = email
#         self.birth_date = birth_date
#
#
# fr1 = Friend("Nika", "597232697", "kldiashvilinika@gmail.com")
# f1 = Family("Giorgi", "555418795", "giorgadzegiorgi@gmail.com", "13/05/2001")
#
# print(f1.birth_date)
# print(fr1.send_mail())
# print(f1.send_mail())


# --------დავალება 5(University with Diamond Problem)--------
# class People:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def get_email(self):
#         return f"{self.first}{self.last}@yahoo.com"
#
#
# class Lecturer(People):
#
#     def __init__(self, first, last, salary):
#         super().__init__(first, last)
#         self.salary = salary
#
#     def get_email(self):
#         super().get_email()
#         return f"{self.first}{self.last}@btu.edu.ge"
#
#
# class Student(People):
#
#     def __init__(self, first, last, courses):
#         super().__init__(first, last)
#         self.courses = courses
#
#     def get_email(self):
#         super().get_email()
#         return f"{self.first}{self.last}.1@btu.edu.ge"
#
#
# class Doctoral_Student(Lecturer, Student):
#
#     def __init__(self, first, last, salary, courses):
#         People.__init__(self, first, last)
#         self.salary = salary
#         self.courses = courses
#
#     def get_email(self):
#         super().get_email()
#         return f"{self.first}{self.last}.2@btu.edu.ge"
#
#
# l1 = Lecturer("Giorgi", "Giorgadze", 3500)
# s1 = Student("Nika", "Kldiashvili", ["Python", "კომპიუტერული ქსელები", "მათემატიკა", "მობილური აპლიკაციები"])
# d1 = Doctoral_Student("Giorgi", "Ciskadze", 1000, ["Python", "მათემატიკა", "მობილური აპლიკაციები"])
# print(d1.get_email())
# # ამ დავალებაში ვერ მივხვდი სად არის Diamond პრობლემა

