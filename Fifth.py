# --------დავალება1--------
# from tkinter import *
#
# win = Tk()
# win.title("First GUI Program")
# win.geometry("450x230+500+200")
# win.configure(bg="#FFFFFF")
#
# Dict = {}
#
#
# def click_register():
#     temp = name.get()
#     temp1 = surname.get()
#     res_text.delete(0.0, END)
#     res_text.insert(0.0, "გამარჯობა, " + temp + " " + temp1 + "!")
#     var1.set("შედეგი: მონაცემები დამატებულია")
#     res_label.configure(fg="red")
#     register.configure(bg="#999999", fg="yellow")
#     name.delete(0, END)
#     surname.delete(0, END)
#     Dict[temp] = temp1
#     print(Dict)
#
#
# Label(win, text="სტუდენტის რეგისტრაციის ფორმა", fg="blue", width=50, height=2, bg="#FFFFFF",
#       font="Calibri 10 bold").grid(row=0, column=0,
#                                    columnspan=2)
# Label(win, text="შეიყვანეთ სახელი:* ", height=2, padx=10, bg="#FFFFFF", font="Calibri 10 bold").grid(row=1, column=0,
#                                                                                                      sticky=W)
#
# var2 = StringVar()
# name = Entry(win, textvariable=var2, relief=GROOVE)
# name.grid(row=1, column=1, sticky=W)
# Label(win, text="შეიყვანეთ გვარი:* ", height=2, padx=10, bg="#FFFFFF", font="Calibri 10 bold").grid(row=2, column=0,
#                                                                                                     sticky=W)
#
# var3 = StringVar()
# surname = Entry(win, textvariable=var3, relief=GROOVE)
# surname.grid(row=2, column=1, sticky=W)
#
# var = StringVar()
# register = Button(win, textvariable=var, relief=GROOVE, width=12, command=click_register)
# register.grid(row=3, column=0)
# var.set("დამატება")
#
# var1 = StringVar()
# res_label = Label(win, textvariable=var1, bg="#FFFFFF", font="Calibri 10")
# res_label.grid(row=3, column=1)
# var1.set("შედეგი: მონაცემები ჯერ არ დამატებულა")
#
# res_text = Text(win, relief=FLAT, height=5, width=30)
# res_text.grid(row=4, column=0, columnspan=2, sticky=W, padx=10, pady=10)
# win.mainloop()


# --------დავალება 2--------
# from tkinter import *
#
# win = Tk()
# win.title("Currency")
# win.geometry("420x350+500+200")
# win.configure(bg="#FFFFFF")
# win.resizable(0, 0)
#
#
# class Currency:
#     Dict_GEL = {"USD": 2.7, "EUR": 3}
#     Dict_USD = {"EUR": 1.11, "GEL": 0.37}
#     Dict_EUR = {"USD": 0.9, "GEL": 0.33}
#
#     def __init__(self, value, unit):
#         self.value = value
#         self.unit = unit
#
#     def __str__(self):
#         return f"{round(self.value, 2)} {self.unit}"
#
#     @staticmethod
#     def changeTo():
#         text.delete(0.0, END)
#         if fromm.get() == "GEL":
#             for k, v in Currency.Dict_GEL.items():
#                 if k == to.get():
#                     new = float(amount.get()) / v
#                     text.insert(0.0, Currency(new, to.get()))
#         elif fromm.get() == "USD":
#             for k, v in Currency.Dict_USD.items():
#                 if k == to.get():
#                     new = float(amount.get()) / v
#                     text.insert(0.0, Currency(new, to.get()))
#         elif fromm.get() == "EUR":
#             for k, v in Currency.Dict_EUR.items():
#                 if k == to.get():
#                     new = float(amount.get()) / v
#                     text.insert(0.0, Currency(new, to.get()))
#         else:
#             var.set("შესაბამისი ვალუტა არ არის რეგისტრირებული")
#             res_label.configure(fg="red")
#
#
# c = Currency(win, None)
#
# Label(win, text="თანხის კონვერტაცია", font="arial 12", fg="blue", height=2, padx=120, bg="white").grid(row=0, column=0,
#                                                                                                        columnspan=2)
# Label(win, text="შეიყვანეთ თანხა", font="arial 12", height=3, padx=30, bg="white").grid(row=1, column=0, sticky=W)
#
# amount = Entry(win, relief=SOLID)
# amount.grid(row=1, column=1, sticky=W, ipadx=25)
#
# Label(win, text="საიდან", font="arial 12", padx=30, bg="white").grid(row=2, column=0, sticky=W)
#
# fromm = Entry(win, relief=SOLID)
# fromm.grid(row=2, column=1, sticky=W, ipadx=25)
#
# Label(win, text="სად", font="arial 12", height=3, padx=30, bg="white").grid(row=3, column=0, sticky=W)
#
# to = Entry(win, relief=SOLID)
# to.grid(row=3, column=1, sticky=W, ipadx=25)
#
# convert = Button(win, text="კონვერტაცია", command=Currency.changeTo, font="arial 12", padx=10,
#                  bg="white", fg="blue", relief=GROOVE)
# convert.grid(row=5, column=0, padx=70, columnspan=2, sticky=W)
#
# var = StringVar()
# res_label = Label(win, textvariable=var, font="arial, 9", bg="white", fg="green")
# res_label.grid(row=4, column=0, columnspan=2, sticky=W, padx=50)
# var.set("შეიყვანეთ სასურველი ვალუტა")
#
# text = Text(win, relief=FLAT, width=30, height=4, font="arial 12")
# text.grid(row=6, column=0, columnspan=2, sticky=W, pady=25, padx=30)
#
# win.mainloop()

# --------დავალება 3--------
from tkinter import *

win = Tk()
win.title("Dictionary")
win.geometry("400x250+500+200")
win.configure(bg="white")

# ფაილში ჩაწერილია სიტყვები: car, book, table
DataFile = open(r"C:\Users\kldia\OneDrive\Desktop\Python Programs\Dictionary.txt", "r", encoding="UTF-8")
Dict = {}
NewDataFile = open(r"C:\Users\kldia\OneDrive\Desktop\Python Programs\New_Words.txt", "a")

for line in DataFile:
    (k, v) = line.split()
    Dict[k] = v


def translate():
    temp = res_entry.get()
    res_text.delete(0.0, END)
    for key, val in Dict.items():
        if key == temp:
            res_text.insert(0.0, val)
            break
    else:
        res_text.insert(0.0, "სიტყვა არ არის დამატებული ლექსიკონში")
        NewDataFile.write(temp + "\n")


Label(win, text="შეიყვანეთ სიტყვა: ", padx=10, height=2, font="Calibri 10", bg="white").grid(row=0, column=0, sticky=W)

var = StringVar()
res_entry = Entry(win, textvariable=var, relief=SOLID, width=25, fg="blue")
res_entry.grid(row=1, column=0, pady=5, padx=10)

Button(win, text="გადათარგმნა", relief=GROOVE, command=translate, font="Calibri 10").grid(row=1, column=1, padx=10)

var1 = StringVar()
res_text = Text(win, height=4, width=37, relief=FLAT, font="Calibri 10 bold")
res_text.grid(row=2, column=0, sticky=W, columnspan=2, padx=10, pady=20)
win.mainloop()


# --------დავალება 4--------
# from tkinter import *
# import math
#
# win = Tk()
# win.title("Calculator")
# win.geometry("295x400+300+150")
# win.resizable(0, 0)
# win.configure(bg="#F9EDED")
# win.iconbitmap(r"C:\Users\kldia\OneDrive\Desktop\Python Programs\ico file\Calculator.ico")
#
# d = {1: "+", 2: "-", 3: "x", 4: "/", 5: "**", 6: "sqrt"}
#
#
# def click_0():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(17, 0)
#             break
#     else:
#         res_entry1.insert(17, 0)
#
#
# def click_1():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(17, 1)
#             break
#     else:
#         res_entry1.insert(17, 1)
#
#
# def click_2():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(17, 2)
#             break
#     else:
#         res_entry1.insert(17, 2)
#
#
# def click_3():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(17, 3)
#             break
#     else:
#         res_entry1.insert(17, 3)
#
#
# def click_4():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(17, 4)
#             break
#     else:
#         res_entry1.insert(17, 4)
#
#
# def click_5():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(17, 5)
#             break
#     else:
#         res_entry1.insert(17, 5)
#
#
# def click_6():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(17, 6)
#             break
#     else:
#         res_entry1.insert(17, 6)
#
#
# def click_7():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(17, 7)
#             break
#     else:
#         res_entry1.insert(17, 7)
#
#
# def click_8():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(17, 8)
#             break
#     else:
#         res_entry1.insert(17, 8)
#
#
# def click_9():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(17, 9)
#             break
#     else:
#         res_entry1.insert(17, 9)
#
#
# def click_dot():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(17, ".")
#             break
#     else:
#         res_entry1.insert(17, ".")
#
#
# def click_pow():
#     res_entry2.insert(0, "**")
#
#
# def click_add():
#     res_entry2.insert(0, "+")
#
#
# def click_mul():
#     res_entry2.insert(0, "x")
#
#
# def click_div():
#     res_entry2.insert(0, "/")
#
#
# def click_sub():
#     res_entry2.insert(0, "-")
#
#
# def click_sqrt():
#     res_entry2.insert(0, "sqrt")
#
#
# def click_neg():
#     temp = res_entry2.get()
#     for k, v in d.items():
#         if v == temp:
#             res_entry3.insert(0, "-")
#             break
#     else:
#         res_entry1.insert(0, "-")
#
#
# def click_C():
#     res_entry1.delete(0, END)
#     res_entry2.delete(0, END)
#     res_entry3.delete(0, END)
#
#
# def click_eq():
#     temp = res_entry2.get()
#     temp1 = res_entry1.get()
#     temp2 = res_entry3.get()
#     if temp == "+":
#         res_entry2.delete(0, END)
#         add = float(temp1) + float(temp2)
#         res_entry2.insert(0, add)
#     elif temp == "-":
#         res_entry2.delete(0, END)
#         sub = float(temp1) - float(temp2)
#         res_entry2.insert(0, sub)
#     elif temp == "x":
#         res_entry2.delete(0, END)
#         mul = float(temp1) * float(temp2)
#         res_entry2.insert(0, mul)
#     elif temp == "/":
#         res_entry2.delete(0, END)
#         div = float(temp1) / float(temp2)
#         res_entry2.insert(0, div)
#     elif temp == "**":
#         res_entry2.delete(0, END)
#         p = float(temp1) ** float(temp2)
#         res_entry2.insert(0, p)
#     elif temp == "sqrt":
#         s = math.sqrt(float(temp1))
#         res_entry3.insert(0, s)
#
#
# res_entry1 = Entry(win, width=19, relief=FLAT, bg="#F9EDED", font="arial 20 bold", justify="right")
# res_entry1.grid(row=0, column=0, columnspan=4)
#
# res_entry2 = Entry(win, width=19, relief=FLAT, bg="#F9EDED", font="arial 20 bold", justify="right")
# res_entry2.grid(row=1, column=0, columnspan=4)
#
# res_entry3 = Entry(win, width=19, relief=FLAT, bg="#F9EDED", font="arial 20 bold", justify="right")
# res_entry3.grid(row=2, column=0, columnspan=4)
#
# button_C = Button(win, text="C", command=click_C, padx=20, pady=12, relief=FLAT, bg="#F0CFCF",
#                   font="arial 12")
# button_C.grid(row=3, column=0, sticky=W, padx=4)
#
# button_pow = Button(win, text="**", command=click_pow, padx=21, pady=12, relief=FLAT, bg="#986A6A",
#                     font="arial 12")
# button_pow.grid(row=3, column=1, sticky=W, padx=4)
#
# button_sqrt = Button(win, text="sq", command=click_sqrt, padx=19, pady=12, relief=FLAT, bg="#F0CFCF", font="arial 12")
# button_sqrt.grid(row=3, column=2, sticky=W, padx=4)
#
# button_div = Button(win, text="/", command=click_div, padx=25, pady=12, relief=FLAT, bg="#986A6A", font="arial 12")
# button_div.grid(row=3, column=3, sticky=W, padx=4)
#
# button_7 = Button(win, text="7", command=click_7, padx=21, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_7.grid(row=4, column=0, sticky=W, padx=4, pady=4)
#
# button_8 = Button(win, text="8", command=click_8, padx=22, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_8.grid(row=4, column=1, sticky=W, padx=4, pady=4)
#
# button_9 = Button(win, text="9", command=click_9, padx=23, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_9.grid(row=4, column=2, sticky=W, padx=4, pady=4)
#
# button_mul = Button(win, text="x", command=click_mul, padx=23, pady=12, relief=FLAT, bg="#F0CFCF", font="arial 12")
# button_mul.grid(row=4, column=3, sticky=W, padx=4, pady=4)
#
# button_4 = Button(win, text="4", command=click_4, padx=21, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_4.grid(row=5, column=0, sticky=W, padx=4)
#
# button_5 = Button(win, text="5", command=click_5, padx=22, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_5.grid(row=5, column=1, sticky=W, padx=4)
#
# button_6 = Button(win, text="6", command=click_6, padx=23, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_6.grid(row=5, column=2, sticky=W, padx=4)
#
# button_sub = Button(win, text="-", command=click_sub, padx=24, pady=12, relief=FLAT, bg="#986A6A", font="arial 12")
# button_sub.grid(row=5, column=3, sticky=W, padx=4)
#
# button_1 = Button(win, text="1", command=click_1, padx=21, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_1.grid(row=6, column=0, sticky=W, padx=4, pady=4)
#
# button_2 = Button(win, text="2", command=click_2, padx=22, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_2.grid(row=6, column=1, sticky=W, padx=4, pady=4)
#
# button_3 = Button(win, text="3", command=click_3, padx=23, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_3.grid(row=6, column=2, sticky=W, padx=4, pady=4)
#
# button_add = Button(win, text="+", command=click_add, padx=22, pady=12, relief=FLAT, bg="#F0CFCF",
#                     font="arial 12")
# button_add.grid(row=6, column=3, sticky=W, padx=4, pady=4)
#
# button_neg = Button(win, text="+/-", command=click_neg, padx=17, pady=12, relief=FLAT, bg="white", font="arial 12",
#                     activebackground="#782C2C")
# button_neg.grid(row=7, column=0, sticky=W, padx=4)
#
# button_0 = Button(win, text="0", command=click_0, padx=22, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_0.grid(row=7, column=1, sticky=W, padx=4)
#
# button_dot = Button(win, text=".", command=click_dot, padx=25, pady=12, relief=FLAT, bg="white",
#                     font="arial 12 bold", activebackground="#782C2C")
# button_dot.grid(row=7, column=2, sticky=W, padx=4)
#
# button_eq = Button(win, text="=", command=click_eq, padx=22, pady=12, relief=FLAT, bg="#986A6A", font="arial 12")
# button_eq.grid(row=7, column=3, sticky=W, padx=4)
#
# win.mainloop()
