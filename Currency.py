from tkinter import *

win = Tk()
win.title("Currency")
win.geometry("420x350+500+200")
win.configure(bg="#FFFFFF")
win.resizable(0, 0)


class Currency:
    Dict_GEL = {"USD": 2.7, "EUR": 3}
    Dict_USD = {"EUR": 1.11, "GEL": 0.37}
    Dict_EUR = {"USD": 0.9, "GEL": 0.33}

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{round(self.value, 2)} {self.unit}"

    @staticmethod
    def changeTo():
        text.delete(0.0, END)
        if fromm.get() == "GEL":
            for k, v in Currency.Dict_GEL.items():
                if k == to.get():
                    new = float(amount.get()) / v
                    text.insert(0.0, Currency(new, to.get()))
        elif fromm.get() == "USD":
            for k, v in Currency.Dict_USD.items():
                if k == to.get():
                    new = float(amount.get()) / v
                    text.insert(0.0, Currency(new, to.get()))
        elif fromm.get() == "EUR":
            for k, v in Currency.Dict_EUR.items():
                if k == to.get():
                    new = float(amount.get()) / v
                    text.insert(0.0, Currency(new, to.get()))
        else:
            var.set("შესაბამისი ვალუტა არ არის რეგისტრირებული")
            res_label.configure(fg="red")


c = Currency(win, None)

Label(win, text="თანხის კონვერტაცია", font="arial 12", fg="blue", height=2, padx=120, bg="white").grid(row=0, column=0,
                                                                                                       columnspan=2)
Label(win, text="შეიყვანეთ თანხა", font="arial 12", height=3, padx=30, bg="white").grid(row=1, column=0, sticky=W)

amount = Entry(win, relief=SOLID)
amount.grid(row=1, column=1, sticky=W, ipadx=25)

Label(win, text="საიდან", font="arial 12", padx=30, bg="white").grid(row=2, column=0, sticky=W)

fromm = Entry(win, relief=SOLID)
fromm.grid(row=2, column=1, sticky=W, ipadx=25)

Label(win, text="სად", font="arial 12", height=3, padx=30, bg="white").grid(row=3, column=0, sticky=W)

to = Entry(win, relief=SOLID)
to.grid(row=3, column=1, sticky=W, ipadx=25)

convert = Button(win, text="კონვერტაცია", command=Currency.changeTo, font="arial 12", padx=10,
                 bg="white", fg="blue", relief=GROOVE)
convert.grid(row=5, column=0, padx=70, columnspan=2, sticky=W)

var = StringVar()
res_label = Label(win, textvariable=var, font="arial, 9", bg="white", fg="green")
res_label.grid(row=4, column=0, columnspan=2, sticky=W, padx=50)
var.set("შეიყვანეთ სასურველი ვალუტა")

text = Text(win, relief=FLAT, width=30, height=4, font="arial 12")
text.grid(row=6, column=0, columnspan=2, sticky=W, pady=25, padx=30)

win.mainloop()
