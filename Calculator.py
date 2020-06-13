from tkinter import *
import math

win = Tk()
win.geometry("295x400+300+150")
win.title("Calculator")
win.configure(bg="#E5E4E4")
win.iconbitmap(r"ico file\Calculator.ico")


def click_clear():
    global entry
    entry = ""
    res_entry.delete(0, END)


def click_btn(numbers):
    global entry
    entry += str(numbers)
    var.set(entry)


def click_equal():
    global entry
    equal = str(eval(entry))
    var.set(equal)
    entry = ""


def click_sqrt():
    sqrt = float(res_entry.get())
    s = math.sqrt(sqrt)
    var.set(s)


entry = ""
var = StringVar()
res_entry = Entry(win, textvariable=var, relief=FLAT, bg="#E5E4E4", justify="right", font="arial 19 bold")
res_entry.grid(row=0, column=0, ipadx=5, ipady=36, columnspan=4)

button_C = Button(win, text="C", command=click_clear, padx=20, pady=12, relief=FLAT, bg="#F0CFCF",
                  font="arial 12")
button_C.grid(row=3, column=0, sticky=W, padx=4)

button_pow = Button(win, text="**", command=lambda: click_btn("**"), padx=21, pady=12, relief=FLAT, bg="#986A6A",
                    font="arial 12")
button_pow.grid(row=3, column=1, sticky=W, padx=4)

button_sqrt = Button(win, text="sq", command=click_sqrt, padx=19, pady=12, relief=FLAT, bg="#F0CFCF",
                     font="arial 12")
button_sqrt.grid(row=3, column=2, sticky=W, padx=4)

button_div = Button(win, text="/", command=lambda: click_btn("/"), padx=25, pady=12, relief=FLAT, bg="#986A6A",
                    font="arial 12")
button_div.grid(row=3, column=3, sticky=W, padx=4)

button_7 = Button(win, text="7", command=lambda: click_btn(7), padx=21, pady=12, relief=FLAT, bg="white",
                  font="arial 12 bold", activebackground="#782C2C")
button_7.grid(row=4, column=0, sticky=W, padx=4, pady=4)

button_8 = Button(win, text="8", command=lambda: click_btn(8), padx=22, pady=12, relief=FLAT, bg="white",
                  font="arial 12 bold", activebackground="#782C2C")
button_8.grid(row=4, column=1, sticky=W, padx=4, pady=4)

button_9 = Button(win, text="9", command=lambda: click_btn(9), padx=23, pady=12, relief=FLAT, bg="white",
                  font="arial 12 bold", activebackground="#782C2C")
button_9.grid(row=4, column=2, sticky=W, padx=4, pady=4)

button_mul = Button(win, text="x", command=lambda: click_btn("*"), padx=23, pady=12, relief=FLAT, bg="#F0CFCF",
                    font="arial 12")
button_mul.grid(row=4, column=3, sticky=W, padx=4, pady=4)

button_4 = Button(win, text="4", command=lambda: click_btn(4), padx=21, pady=12, relief=FLAT, bg="white",
                  font="arial 12 bold", activebackground="#782C2C")
button_4.grid(row=5, column=0, sticky=W, padx=4)

button_5 = Button(win, text="5", command=lambda: click_btn(5), padx=22, pady=12, relief=FLAT, bg="white",
                  font="arial 12 bold", activebackground="#782C2C")
button_5.grid(row=5, column=1, sticky=W, padx=4)

button_6 = Button(win, text="6", command=lambda: click_btn(6), padx=23, pady=12, relief=FLAT, bg="white",
                  font="arial 12 bold", activebackground="#782C2C")
button_6.grid(row=5, column=2, sticky=W, padx=4)

button_sub = Button(win, text="-", command=lambda: click_btn("-"), padx=24, pady=12, relief=FLAT, bg="#986A6A",
                    font="arial 12")
button_sub.grid(row=5, column=3, sticky=W, padx=4)

button_1 = Button(win, text="1", command=lambda: click_btn(1), padx=21, pady=12, relief=FLAT, bg="white",
                  font="arial 12 bold", activebackground="#782C2C")
button_1.grid(row=6, column=0, sticky=W, padx=4, pady=4)

button_2 = Button(win, text="2", command=lambda: click_btn(2), padx=22, pady=12, relief=FLAT, bg="white",
                  font="arial 12 bold", activebackground="#782C2C")
button_2.grid(row=6, column=1, sticky=W, padx=4, pady=4)

button_3 = Button(win, text="3", command=lambda: click_btn(3), padx=23, pady=12, relief=FLAT, bg="white",
                  font="arial 12 bold", activebackground="#782C2C")
button_3.grid(row=6, column=2, sticky=W, padx=4, pady=4)

button_add = Button(win, text="+", command=lambda: click_btn("+"), padx=22, pady=12, relief=FLAT, bg="#F0CFCF",
                    font="arial 12")
button_add.grid(row=6, column=3, sticky=W, padx=4, pady=4)

button_neg = Button(win, text="+/-", command=lambda: click_btn("-"), padx=17, pady=12, relief=FLAT, bg="white",
                    font="arial 12",
                    activebackground="#782C2C")
button_neg.grid(row=7, column=0, sticky=W, padx=4)

button_0 = Button(win, text="0", command=lambda: click_btn(0), padx=22, pady=12, relief=FLAT, bg="white",
                  font="arial 12 bold", activebackground="#782C2C")
button_0.grid(row=7, column=1, sticky=W, padx=4)

button_dot = Button(win, text=".", command=lambda: click_btn("."), padx=25, pady=12, relief=FLAT, bg="white",
                    font="arial 12 bold", activebackground="#782C2C")
button_dot.grid(row=7, column=2, sticky=W, padx=4)

button_eq = Button(win, text="=", command=click_equal, padx=22, pady=12, relief=FLAT, bg="#986A6A", font="arial 12")
button_eq.grid(row=7, column=3, sticky=W, padx=4)

win.mainloop()
