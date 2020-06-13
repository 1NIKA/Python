import tkinter as tk
from tkinter import ttk


# -------- დავალება 1--------
class Weather:
    def __init__(self, temperature, unit, humidity=None):
        self.temperature = temperature
        self.unit = unit
        self.humidity = humidity

    def __str__(self):
        if self.humidity is None:
            return f"ტემპერატურა: {self.temperature} {self.unit}; ტენიანობა: 0%"
        else:
            return f"ტემპერატურა: {self.temperature} {self.unit}; ტენიანობა: {self.humidity}%"

    def change_unit(self):
        if self.unit == "F":
            new_c = (self.temperature - 32) / 1.8
            return Weather(new_c, "C", self.humidity)
        else:
            return Weather(self.temperature, self.unit, self.humidity)

    def discomfort(self):
        if self.unit == "C":
            discomfort1 = self.temperature - 0.55 * (1 - 0.01 * self.humidity) * (self.temperature - 14.5)
            return discomfort1
        else:
            pass

    def __gt__(self, other):
        if self.temperature > other.temperature:
            return True
        else:
            return False


c1 = Weather(32, "C", 19)
c2 = Weather(30, "F")
print(c1.change_unit())
print(c2.change_unit())
c1.discomfort()
print(c1 > c2)


def discomfort():
    if var.get() == 1:
        t1 = float(temperature1.get())
        h1 = float(humidity1.get())
        c3 = Weather(t1, "C", h1)
        var1.set(c3.discomfort())

        if float(var1.get()) < 21:
            var2.set("დისკომფორტის გარეშე")
        if 21 <= float(var1.get()) < 24:
            var2.set("მცირე დისკომფორტია")
        if 24 <= float(var1.get()) < 29:
            var2.set("საყურადღებო დისკომფორტია")
        if 29 <= float(var1.get()) < 32:
            var2.set("ყველა განიცდის დისკომფორტს")
        if float(var1.get()) >= 32:
            var2.set("საგანგებო მდგომარეობაა")
    else:
        var1.set("")
        var2.set("გთხოვთ აირჩიოთ ცელსიუსი")


win = tk.Tk()
win.title("დისკომფორტის ინდექსი")
win.geometry("400x300+500+200")

ttk.Label(win, text="ტემპერატურა").grid(row=0, column=0, sticky="w", pady=15, padx=10)
ttk.Label(win, text="ტენიანობა").grid(row=1, column=0, sticky="w", pady=10, padx=10)
ttk.Label(win, text="%").grid(row=1, column=2, sticky="w", pady=10)

temperature1 = ttk.Entry(win, width=6)
temperature1.grid(row=0, column=1, sticky="w")
humidity1 = ttk.Entry(win, width=6)
humidity1.grid(row=1, column=1, sticky="w")

var = tk.IntVar()
r1 = ttk.Radiobutton(win, text="C", variable=var, value=1)
r1.grid(row=0, column=3, sticky="w")
r2 = ttk.Radiobutton(win, text="F", variable=var, value=2)
r2.grid(row=0, column=4, padx=10, sticky="w")

result = ttk.Button(win, text="გამოთვლა", command=discomfort)
result.grid(row=2, column=1, columnspan=4, sticky="w", pady=10)

ttk.Label(win, text="დისკომფორტის ინდექსი: ").grid(row=3, column=0, sticky="w", columnspan=4, pady=15, padx=10)
ttk.Label(win, text="დისკომფორტის აღწერა: ").grid(row=4, column=0, sticky="w", columnspan=4, padx=10)

var1 = tk.StringVar()
var1.set("")
result1 = ttk.Label(win, textvariable=var1).grid(row=3, column=4, sticky="w", columnspan=4, padx=7)
var2 = tk.StringVar()
var2.set("")
result2 = ttk.Label(win, textvariable=var2).grid(row=4, column=4, sticky="w", columnspan=4, padx=7)

win.mainloop()

import tkinter as tk
from tkinter import ttk


class Service:
    def __init__(self, service_name, price, tip, quantity):
        self.service_name = service_name
        self.price = price
        self.tip = tip
        self.quantity = quantity

    def __str__(self):
        return f"მომსახურეობა: {self.service_name}, სრული ღირებულება: {self.price} ლარი, მომსახურების ნაჩუქარი თანხა (Tip): {self.tip}%, ადამიანების რაოდენობა: {self.quantity}"

    def tip_price(self):
        return f"{(self.price * self.tip) / 100} ლარი"

    def tip_price2(self):
        return f"{((self.price * self.tip) / 100) / self.quantity} ლარი"

    def service_price(self):
        return f"{self.price + (self.price * self.tip) / 100} ლარი"

    def service_price2(self):
        return f"{(self.price + (self.price * self.tip) / 100) / self.quantity} ლარი"

    def __le__(self, other):
        if s1.service_price2() <= s2.service_price2():
            return True
        else:
            return False


s1 = Service("Food Delivery", 110, 10, 2)
s2 = Service("Taxi", 500, 10, 5)
print(s1)
print(s1.tip_price())
print(s1.tip_price2())
print(s2.service_price())
print(s2.service_price2())
print(s1 <= s2)


def click_result():
    p = float(price1.get())
    t = float(tip1.get())
    q = float(quantity1.get())
    s3 = Service("Service", p, t, q)
    var1.set(s3.tip_price())
    var2.set(s3.tip_price2())
    var3.set(s3.service_price())
    var4.set(s3.service_price2())


win = tk.Tk()
win.title("Tip Calculator")
win.geometry("400x300+500+200")

ttk.Label(win, text="მომსახურების ღირებულება: ").grid(row=0, column=0, sticky="w", padx=10, pady=10)
ttk.Label(win, text="Tip %: ").grid(row=1, column=0, sticky="w", padx=10)
ttk.Label(win, text="ადამიანების რაოდენობა: ").grid(row=2, column=0, sticky="w", padx=10, pady=10)
ttk.Label(win, text="ლარი").grid(row=0, column=2, sticky="w", pady=10)
ttk.Label(win, text="%").grid(row=1, column=2, sticky="w")

price1 = ttk.Entry(win, width=9)
price1.grid(row=0, column=1)
tip1 = ttk.Entry(win, width=9)
tip1.grid(row=1, column=1)
quantity1 = ttk.Entry(win, width=9)
quantity1.grid(row=2, column=1)

result = ttk.Button(win, text="გამოთვლა", command=click_result)
result.grid(row=3, column=0, columnspan=2, pady=10)

ttk.Label(win, text="მომს.ნაჩუქარი თანხა (Tip): ").grid(row=4, column=0, sticky="w", padx=10, pady=10)
ttk.Label(win, text="Tip თითო კაცზე: ").grid(row=5, column=0, sticky="w", padx=10)
ttk.Label(win, text="ჯამური გადასახადი: ").grid(row=6, column=0, sticky="w", padx=10, pady=10)
ttk.Label(win, text="გადასახადი თითო კაცზე: ").grid(row=7, column=0, sticky="w", padx=10)

var1 = tk.StringVar()
var1.set("")
ttk.Label(win, textvariable=var1).grid(row=4, column=1, sticky="w", padx=10, pady=10, columnspan=4)
var2 = tk.StringVar()
var2.set("")
ttk.Label(win, textvariable=var2).grid(row=5, column=1, sticky="w", padx=10, columnspan=4)
var3 = tk.StringVar()
var3.set("")
ttk.Label(win, textvariable=var3).grid(row=6, column=1, sticky="w", padx=10, pady=10, columnspan=4)
var4 = tk.StringVar()
var4.set("")
ttk.Label(win, textvariable=var4).grid(row=7, column=1, sticky="w", padx=10, columnspan=4)

win.mainloop()
