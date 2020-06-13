# # --------დავალება 1--------
# class Cat:
#     def eat(self):
#         print("Cat eats a milk")
#
#     def talk(self):
#         print("Cat says miaow")
#
#     def walk(self):
#         print("Cat can run 20km/h")
#
#
# class Dog:
#     def eat(self):
#         print("Dog eats a bone")
#
#     def talk(self):
#         print("Dog says Aww")
#
#     def walk(self):
#         print("Dog can run 40km/h")
#
#
# def dinner(obj):
#     obj.eat()
#
#
# def Talk(obj):
#     obj.talk()
#
#
# def Walk(obj):
#     obj.walk()
#
#
# c1 = Cat()
# d1 = Dog()
# dinner(c1)
# dinner(d1)
# Talk(c1)
# Talk(d1)
# Walk(c1)
# Walk(d1)


# --------დავალება 2--------
class Currency:
    Dict_GEL = {"USD": 2.7, "EUR": 3}
    Dict_USD = {"EUR": 1.11, "GEL": 0.37}
    Dict_EUR = {"USD": 0.9, "GEL": 0.33}

    def __init__(self, value, unit="GEL"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def changeGEL(self, other):
        if other == "USD":
            gel = self.value / self.Dict_GEL["USD"]
            return round(gel, 2)
        elif other == "EUR":
            gel = self.value / self.Dict_GEL["EUR"]
            return round(gel, 2)
        else:
            print("მოცემული ვალუტა არ არსებობს")

    def changeUSD(self, other):
        if other == "EUR":
            usd = self.value / self.Dict_USD["EUR"]
            return round(usd, 2)
        elif other == "GEL":
            usd = self.value / self.Dict_USD["GEL"]
            return round(usd, 2)
        else:
            print("მოცემული ვალუტა არ არსებობს")

    def changeEUR(self, other):
        if other == "USD":
            eur = self.value / self.Dict_EUR["USD"]
            return round(eur, 2)
        elif other == "GEL":
            eur = self.value / self.Dict_EUR["GEL"]
            return round(eur, 2)
        else:
            print("მოცემული ვალუტა არ არსებობს")

    def __add__(self, other):
        if isinstance(other, Currency):
            new_value = self.value + other.value
            new_unit = self.unit
        else:
            new_value = self.value + other
            new_unit = self.unit
            return Currency(round(new_value, 2), new_unit)
        if self.unit == other.unit:
            new_value = self.value + other.value
            new_unit = self.unit
            return Currency(round(new_value, 2), new_unit)
        if self.unit != other.unit:
            if self.unit == "USD" and other.unit == "EUR":
                new_currency = Currency.changeEUR(other, "USD")
                new_value = self.value + new_currency
                new_unit = self.unit
                return Currency(new_value, new_unit)
        if self.unit != other.unit:
            if self.unit == "USD" and other.unit == "GEL":
                new_currency = Currency.changeGEL(other, "USD")
                new_value = self.value + new_currency
                new_unit = self.unit
                return Currency(new_value, new_unit)
        if self.unit != other.unit:
            if self.unit == "EUR" and other.unit == "GEL":
                new_currency = Currency.changeGEL(other, "EUR")
                new_value = self.value + new_currency
                new_unit = self.unit
                return Currency(new_value, new_unit)
        if self.unit != other.unit:
            if self.unit == "EUR" and other.unit == "USD":
                new_currency = Currency.changeUSD(other, "EUR")
                new_value = self.value + new_currency
                new_unit = self.unit
                return Currency(new_value, new_unit)
        if self.unit != other.unit:
            if self.unit == "GEL" and other.unit == "USD":
                new_currency = Currency.changeUSD(other, "GEL")
                new_value = self.value + new_currency
                new_unit = self.unit
                return Currency(new_value, new_unit)
        if self.unit != other.unit:
            if self.unit == "GEL" and other.unit == "EUR":
                new_currency = Currency.changeEUR(other, "GEL")
                new_value = self.value + new_currency
                new_unit = self.unit
                return Currency(new_value, new_unit)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        try:
            if isinstance(other, int) or isinstance(other, float):
                new_value = self.value * other
                new_unit = self.unit
                return Currency(new_value, new_unit)
        except TypeError:
            print("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __gt__(self, other):
        if self.value > other.value:
            print("თანხა მეტია")
        else:
            print("თანხა ნაკლებია")


obj1 = Currency(400)
obj2 = Currency(100, "USD")
obj3 = Currency(200, "EUR")
print(obj1)
print(obj1.changeGEL("USD"))
print(obj2 + obj3)
sum_obj = obj2 + 100
print(sum_obj)
sum_obj = obj3 * 2
print(sum_obj)
sum_obj = 2 * obj3
print(sum_obj)
obj2.__gt__(obj3)

# 00-ბი როგორ დავუწერო ვერ მივხვდი და კიდევ კონვერტაციის შემდეგ იმ ვალუტას არ წერს.
