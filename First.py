# # --------davaleba 1--------
# class Rectangle:
#     def __init__(self, width, length, color):
#         self.width = width
#         self.length = length
#         self.color = color
#
#     def perimeter(self):
#         return 2 * (self.width + self.length)
#
#     def area(self):
#         return self.width * self.length
#
# obj1 = Rectangle(1, 5, "blue")
# obj2 = Rectangle(3, 3, "green")
# obj3 = Rectangle(3, 7, "purple")
#
# print(obj1.area())
#
#
#
#
#
#
#
# # --------davaleba 2--------
# class Car:
#     def __init__(self, color, model, makeYear, fuelType, price, Rent):
#         self.color = color
#         self.model = model
#         self.makeYear = makeYear
#         self.fuelType = fuelType
#         self.price = price
#         self.Rent = Rent
#
#     def sell(self):
#         return self.price
#
#     def rent(self):
#         return self.Rent
#
# obj1 = Car("red", "Mercedes", 2015, "Gas", "25000€", "200€")
# obj2 = Car("blue", "BMW", 2013, "Gas", "15000€", "150€")
# obj3 = Car("orange", "Audi", 2009, "Diesel", "18000€", "200€")
#
# print(obj1.sell())
# print(obj1.rent())
# print(obj2.sell())
# print(obj2.rent())
#
#
#
#
#
#
#
#
# # --------davaleba 3--------
# class Dog:
#     def __init__(self, breed, size, age, color):
#         self.Breed = breed
#         self.Size = size
#         self.Age = age
#         self.Color = color
#
#     def Eat(self):
#         return self.Age / 2
#
#     def Sleep(self):
#         return self.Age / 0.7
#
#
# obj1 = Dog("Neapolitan Mastiff", "Large", 5, "Black")
# obj2 = Dog("Maltese", "Small", 2, "White")
# obj3 = Dog("Chow Chow", "Medium", 3, "Brown")
#
# print(obj1.Breed)
# print(obj1.Eat(), "kg")
# print(obj1.Sleep(), "საათი")
#
#
#
#
#
#
#
#
# # --------davaleba 4--------
# class Fraction:
#     def __init__(self, top, bottom):
#         self.top = top
#         self.bottom = bottom
#
#     def __str__(self):
#         return f"{self.top}/{self.bottom}"
#
#     def inverse(self):
#         return Fraction(self.bottom, self.top)
#
#     def sum_fr(self, other):
#         new_top = (self.top * other.bottom) + (other.top * self.bottom)
#         new_bottom = (self.bottom * other.bottom)
#         return Fraction(new_top, new_bottom)
#
#
# f1 = Fraction(1, 2)
# f2 =Fraction(3, 4)
# print(f1)
# print(f2)
# print(f1.inverse())
# print(f1.sum_fr(f2))
#
#
#
#
#
#
#
import math

# #  --------davaleba 5--------
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def length(self):
#         return math.sqrt((self.x ** 2) + (self.y ** 2))
#
# obj1 = Point(3, 5)
# obj2 = Point(6, 9)
#
# print(obj1.length())
# print(obj2.length())
#
#
#
#
#
#
#
#  --------davaleba 6--------
x1 = int(input("შეიყვანეთ x1 რიცხვი: "))
y1 = int(input("შეიყვანეთ y1 რიცხვი: "))
x2 = int(input("შეიყვანეთ x2 რიცხვი: "))
y2 = int(input("შეიყვანეთ y2 რიცხვი: "))


class Point:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        return "({},{})".format(self.a, self.b)

    def length(self, ):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


obj1 = Point(x1, y1)
obj2 = Point(x2, y2)
print("A =", obj1.__str__())
print("B =", obj2.__str__())
print("2 წერტილს შორის მანძილია = ", obj1.length())
#
#
#
#
#
#
#
#  --------davaleba 7--------
# class Mydate:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def __str__(self):
#         return "{}/{}/{}".format(self.day, self.month, self.year)
#
#     def difference(self):
#         return (obj1.year - obj2.year) * 12 + (obj1.month - obj2.month)
#
#
# obj1 = Mydate(8, 4, 2010)
# obj2 = Mydate(1, 4, 2009)
# print(obj1.__str__())
# print(obj2.__str__())
# print("თვეების რაოდენობა არის", obj1.difference())
