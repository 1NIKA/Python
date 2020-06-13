# --------დავალება 1--------
# class Celsius:
#
#     def __init__(self, temperature):
#         self.__temperature = temperature
#
#     def get_temp(self):
#         return f"{self.__temperature} C"
#
#     def set_temp(self, text):
#         self.__temperature = text
#
#     def del_temp(self):
#         del self.__temperature
#
#     def difference_temp(self, other):
#         new_temp = (self.__temperature - other.__temperature)
#         return f"განსხვავება ცელსიუსებში არის {abs(new_temp)} C"
#
#     @staticmethod
#     def change_temp(text):
#         return f"{text.__temperature} C = {9 / 5 * text.__temperature + 32} F"
#
#     temperature = property(get_temp, set_temp, del_temp)
#
#
# obj1 = Celsius(10)
# obj2 = Celsius(35)
# obj1.temperature = 30
# print(obj1.temperature)
# print(obj2.temperature)
# print(obj1.difference_temp(obj2))
# print(Celsius.change_temp(obj1))
# print(Celsius.change_temp(obj2))
#
#
# # --------დავალება 2--------
# class Employee:
#     organization = "Google"
#
#     def __init__(self, name, age, salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def email(self):
#         return f"{self.__name}@gmail.com"
#
#     @email.setter
#     def email(self, name):
#         result = name.split()
#         self.__name = result[0]
#
#     def salary(self, other):
#         new_salary = self.__salary + other
#         return new_salary
#
#     @staticmethod
#     def convert_to_usd(salary):
#         return salary.__salary / 3.1
#
#     def salary_in_usd(self):
#         return self.convert_to_usd(obj1)
#
#
# obj1 = Employee("Nika", 18, 3000)
# obj2 = Employee("Luka", 20, 1500)
# print(obj1.name)
# obj1.email = "Davit"
# print(obj1.email)
# print(obj1.name)
# print(obj1.salary(2000), "GEL")
# print(Employee.convert_to_usd(obj2), "USD")
# print(obj1.salary_in_usd(), "USD")


# # # --------დავალება 3--------
# class Bank_Account:
#     def __init__(self, account_name, balance=0):
#         self.__account_name = account_name
#         self.__balance = balance
#
#     def get_name(self):
#         return self.__account_name
#
#     def set_name(self, text):
#         self.__account_name = text
#
#     def deposit(self, other):
#         return f"თანხის შეტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance + other} ლარი"
#
#     def withdraw(self, other):
#         if self.__balance >= other:
#             return f"თანხის გამოტანა შესრულებულია. ამჟამად ანგარიშზე გაქვთ {self.__balance - other} ლარი"
#         else:
#             return "თანხის გამოტანა შეუძლებელია არასაკმარისი ბალანსის გამო."
#
#     name = property(get_name, set_name)
#
#
# Name = input("შეიტანეთ კლიენტის სახელი და გვარი: ")
# Balance = int(input("რა თანხა გაქვთ ამჟამად ანგარიშზე? "))
# Number = input("შეიტანეთ შესაბამისი ციფრი, რომელი ოპერაციის შესრულებაც გსურთ: თანხის შეტანა: 1  თანხის გატანა: 2 ")
#
# obj1 = Bank_Account(Name, Balance)
# obj2 = Bank_Account(Name, Balance)
# if Number == "1":
#     Deposit = int(input("რა თანხის შეტანა გსურთ? "))
#     print(obj1.deposit(Deposit))
# elif Number == "2":
#     Withdraw = int(input("რა თანხის გატანა გსურთ? "))
#     print(obj1.withdraw(Withdraw))
# else:
#     print("არჩეული მოქმედება არ არსებობს")


