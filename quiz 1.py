class Book:
    def __init__(self, title, price, quantity=1):
        self.__title = title
        self.__price = price
        self.__quantity = quantity

    def __str__(self):
        return f"წიგნის სათაური: {self.__title}, ფასი: {self.__price}, რაოდენობა: {self.__quantity} ცალი"

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, text):
        self.__title = text

    def sell(self, other):
        if self.__quantity >= other:
            self.__quantity -= other
            print(f"წარმატებით გაიყიდა, დარჩა {self.__quantity}")
        else:
            return "ბოდიში, ამდენი წიგნი არ გვაქვს"

    @staticmethod
    def time(other):
        time = other / 250
        return f"დაჭირდება {time} წუთი"


# Sell = int(input("რამდენი წიგნი გინდათ? "))
obj1 = Book("Harry Potter", 25, 50)
print(obj1)
print(obj1.title)
obj1.title = "Hamlet"
print(obj1.title)
obj1.sell(15)
obj1.sell(4)
print(obj1.time(8000))
