# -------- დავალება 1--------
# import tkinter
# from tkinter import ttk
#
# win = tkinter.Tk()
# win.geometry("400x520+580+100")
# win.title("სასწავლო წიგნაკი")
# # win.iconbitmap(r"C:\Users\kldia\OneDrive\Desktop\Python Programs\ico file\BTU.ico")
#
# dic = {}
# Registration = open(r"C:\Users\kldia\.android\python\Registration.txt", "a", encoding="UTF-8")
#
#
# def click_add():
#     dic["სახელი"] = name.get()
#     dic["გვარი"] = sur_name.get()
#     dic["დაბ.თარიღი"] = f"{c1.get()} {c2.get()} {c3.get()}"
#     dic["E-mail"] = email.get()
#     dic["ტელეფონი"] = tel.get()
#     dic["ფაკულტეტი"] = c4.get()
#     dic["საფეხური"] = c5.get()
#     dic["კურსი"] = c6.get()
#     Registration.write(str(dic) + "\n")
#     print(dic)
#
#
# def click_reset():
#     name.delete(0, tkinter.END)
#     sur_name.delete(0, tkinter.END)
#     c1.set("წელი")
#     c2.set("თვე")
#     c3.set("დღე")
#     email.delete(0, tkinter.END)
#     tel.delete(0, tkinter.END)
#     c4.set("აირჩიეთ ფაკულტეტი")
#     c5.set("აირჩიეთ საფეხური")
#     c6.set("აირჩიეთ კურსი")
#
#
# def click_destroy():
#     win.destroy()
#
#
# def choose_course():
#     if c5.current() == 0:
#         c6["values"] = ["პროგრამირება Python", "Cisco Packet Tracer", "მობილური აპლიკაციები", "მონაცემთა ბაზები"]
#     elif c5.current() == 1:
#         c6["values"] = ["IT-სერვისების მართვა", "ფინანსური აღრიცხვა"]
#     elif c5.current() == 2:
#         c6["values"] = ["აკადემიური წერა", "სტატისტიკა", "პროსპექტუსი", "ემპირიული მეთოდები", "კვლევის მეთოდები"]
#
#
# nb = ttk.Notebook(win)
# nb.pack(fill="both", expand=1, padx=10, pady=10)
#
# tab1 = ttk.Frame(nb)
# tab2 = ttk.Frame(nb)
# tab3 = ttk.Frame(nb)
#
# nb.add(tab1, text="Registration", underline=0)
# nb.add(tab2, text="All Students", underline=0)
# nb.add(tab3, text="Lectures", underline=0)
#
# lb1 = ttk.LabelFrame(tab1, text="პირადი ინფორმაცია")
# lb1.pack(fill="both", expand=1, pady=15, padx=10)
#
# ttk.Label(lb1, text="სახელი: ").grid(row=0, column=0, padx=10, pady=5, sticky="w")
# ttk.Label(lb1, text="გვარი: ").grid(row=1, column=0, padx=10, pady=5, sticky="w")
# ttk.Label(lb1, text="დაბ.თარიღი:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
# ttk.Label(lb1, text="სქესი: ").grid(row=3, column=0, padx=10, pady=5, sticky="w")
# ttk.Label(lb1, text="E-mail: ").grid(row=4, column=0, padx=10, pady=5, sticky="w")
# ttk.Label(lb1, text="ტელ : ").grid(row=5, column=0, padx=10, pady=5, sticky="w")
# tkinter.Label(tab2, text="პირადი მონაცემების გავრცელების უფლება არ გვაქვს!", fg="purple").grid(row=0, column=0,
#                                                                                                pady=200, padx=20)
# tkinter.Label(tab3, text="დაფარულია ადმინისტრაციის მიერ!", fg="purple").grid(row=0, column=0, pady=200, padx=75)
#
# name = ttk.Entry(lb1)
# name.grid(row=0, column=1, padx=20, ipadx=30, columnspan=3)
# sur_name = ttk.Entry(lb1)
# sur_name.grid(row=1, column=1, padx=20, pady=5, ipadx=30, columnspan=3)
# email = ttk.Entry(lb1)
# email.grid(row=4, column=1, padx=20, pady=5, ipadx=30, columnspan=3)
# tel = ttk.Entry(lb1)
# tel.grid(row=5, column=1, padx=20, pady=5, ipadx=30, columnspan=3)
#
# var1 = tkinter.StringVar()
# var1.set("წელი")
# c1 = ttk.Combobox(lb1, textvariable=var1, width=7, state="readonly")
# c1["values"] = [2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990]
# c1.grid(row=2, column=1, padx=19, sticky="w")
# var2 = tkinter.StringVar()
# var2.set("თვე")
# c2 = ttk.Combobox(lb1, textvariable=var2, width=4, state="readonly")
# c2["values"] = ["იან", "თებ", "მარ", "აპრ", "მაი", "ივნ", "ივლ", "აგვ", "სექ", "ოქტ", "ნოე", "დეკ"]
# c2.grid(row=2, column=2, sticky="w")
# var3 = tkinter.StringVar()
# var3.set("დღე")
# c3 = ttk.Combobox(lb1, textvariable=var3, width=5, state="readonly")
# c3["values"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
#                 29, 30, 31]
# c3.grid(row=2, column=3, padx=10, sticky="w")
#
# rd1 = ttk.Radiobutton(lb1, text="ქალი", value=1)
# rd1.grid(row=3, column=1)
# rd1 = ttk.Radiobutton(lb1, text="კაცი", value=2)
# rd1.grid(row=3, column=2)
#
# lb2 = ttk.LabelFrame(tab1, text="უნივერსიტეტი")
# lb2.pack(fill="both", expand=1, pady=15, padx=10)
#
# ttk.Label(lb2, text="ფაკულტეტი: ").grid(row=0, column=0, padx=10, pady=5, sticky="w")
# ttk.Label(lb2, text="საფეხური: ").grid(row=1, column=0, padx=10, pady=5, sticky="w")
# ttk.Label(lb2, text="კურსი: ").grid(row=2, column=0, padx=10, pady=5, sticky="w")
#
# var4 = tkinter.StringVar()
# var4.set("აირჩიეთ ფაკულტეტი")
# c4 = ttk.Combobox(lb2, textvariable=var4, width=18, state="readonly")
# c4["values"] = ["კომპიუტერული მეცნიერება", "მენეჯმენტი", "ფინანსები"]
# c4.grid(row=0, column=1, padx=16, pady=5, ipadx=31, columnspan=3)
# var5 = tkinter.StringVar()
# var5.set("აირჩიეთ საფეხური")
# c5 = ttk.Combobox(lb2, textvariable=var5, width=18, state="readonly")
# c5["values"] = ["ბაკალავრიატი", "მაგისტრატურა", "დოქტორანტურა"]
# c5.grid(row=1, column=1, padx=16, pady=10, ipadx=31, columnspan=3)
# var6 = tkinter.StringVar()
# var6.set("აირჩიეთ კურსი")
# c6 = ttk.Combobox(lb2, textvariable=var6, width=18, state="readonly", postcommand=choose_course)
# c6.grid(row=2, column=1, padx=16, pady=5, ipadx=31, columnspan=3)
#
# add = ttk.Button(tab1, text="დამატება", command=click_add)
# add.pack(side="left", padx=15)
# reset = ttk.Button(tab1, text="Reset", command=click_reset)
# reset.pack(side="left", padx=15)
# destroy = ttk.Button(tab1, text="ფანჯრის დახურვა", command=click_destroy)
# destroy.pack(side="left", padx=15)
#
# nb.enable_traversal()
# win.mainloop()

# -------- დავალება 2---------
# import tkinter
# from tkinter import ttk
#
# win = tkinter.Tk()
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
#         text.delete(0.0, tkinter.END)
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
# convert = tkinter.Label(win, text="თანხის კონვერტაცია", font="arial 12", fg="blue", height=2, padx=120, bg="white")
# convert.grid(row=0, column=0, columnspan=2)
#
# tkinter.Label(win, text="შეიყვანეთ თანხა", font="arial 12", height=3, padx=30, bg="white").grid(row=1, column=0,
#                                                                                                 sticky="w")
#
# amount = ttk.Entry(win)
# amount.grid(row=1, column=1, sticky="w", ipadx=25)
#
# tkinter.Label(win, text="საიდან", font="arial 12", padx=30, bg="white").grid(row=2, column=0, sticky="w")
#
# var1 = tkinter.StringVar()
# var1.set("აირჩიეთ ვალუტა")
# fromm = ttk.Combobox(win, textvariable=var1)
# fromm["values"] = ["GEL", "USD", "EUR"]
# fromm.grid(row=2, column=1, sticky="w", ipadx=17)
#
# tkinter.Label(win, text="სად", font="arial 12", height=3, padx=30, bg="white").grid(row=3, column=0, sticky="w")
#
# var2 = tkinter.StringVar()
# var2.set("აირჩიეთ ვალუტა")
# to = ttk.Combobox(win, textvariable=var2)
# to["values"] = ["GEL", "USD", "EUR"]
# to.grid(row=3, column=1, sticky="w", ipadx=17)
#
# convert = tkinter.Button(win, text="კონვერტაცია", command=Currency.changeTo, font="arial 12", padx=10,
#                          bg="white", fg="blue", relief="groove")
# convert.grid(row=5, column=0, padx=70, columnspan=2, sticky="w")
#
# var = tkinter.StringVar()
# res_label = tkinter.Label(win, textvariable=var, font="arial, 9", bg="white", fg="green")
# res_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=50)
# var.set("შეიყვანეთ სასურველი ვალუტა")
#
# text = tkinter.Text(win, relief="flat", width=30, height=4, font="arial 12")
# text.grid(row=6, column=0, columnspan=2, sticky="w", pady=25, padx=30)
#
# win.mainloop()

# -------- დავალება 3--------
# from tkinter import *
# import math
#
# win = Tk()
# win.geometry("295x400+300+150")
# win.title("Calculator")
# win.configure(bg="#E5E4E4")
# win.iconbitmap(r"C:\Users\kldia\OneDrive\Desktop\Python Programs\ico file\Calculator.ico")
#
#
# def click_clear():
#     global entry
#     entry = ""
#     res_entry.delete(0, END)
#
#
# def click_btn(numbers):
#     global entry
#     entry += str(numbers)
#     var.set(entry)
#
#
# def click_equal():
#     global entry
#     equal = str(eval(entry))
#     var.set(equal)
#
#
# def click_sqrt():
#     sqrt = float(res_entry.get())
#     s = math.sqrt(sqrt)
#     var.set(s)
#
#
# entry = ""
# var = StringVar()
# res_entry = Entry(win, textvariable=var, relief=FLAT, bg="#E5E4E4", justify="right", font="arial 19 bold")
# res_entry.grid(row=0, column=0, ipadx=5, ipady=36, columnspan=4)
#
# button_C = Button(win, text="C", command=click_clear, padx=20, pady=12, relief=FLAT, bg="#F0CFCF",
#                   font="arial 12")
# button_C.grid(row=3, column=0, sticky=W, padx=4)
#
# button_pow = Button(win, text="**", command=lambda: click_btn("**"), padx=21, pady=12, relief=FLAT, bg="#986A6A",
#                     font="arial 12")
# button_pow.grid(row=3, column=1, sticky=W, padx=4)
#
# button_sqrt = Button(win, text="sq", command=click_sqrt, padx=19, pady=12, relief=FLAT, bg="#F0CFCF",
#                      font="arial 12")
# button_sqrt.grid(row=3, column=2, sticky=W, padx=4)
#
# button_div = Button(win, text="/", command=lambda: click_btn("/"), padx=25, pady=12, relief=FLAT, bg="#986A6A",
#                     font="arial 12")
# button_div.grid(row=3, column=3, sticky=W, padx=4)
#
# button_7 = Button(win, text="7", command=lambda: click_btn(7), padx=21, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_7.grid(row=4, column=0, sticky=W, padx=4, pady=4)
#
# button_8 = Button(win, text="8", command=lambda: click_btn(8), padx=22, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_8.grid(row=4, column=1, sticky=W, padx=4, pady=4)
#
# button_9 = Button(win, text="9", command=lambda: click_btn(9), padx=23, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_9.grid(row=4, column=2, sticky=W, padx=4, pady=4)
#
# button_mul = Button(win, text="x", command=lambda: click_btn("*"), padx=23, pady=12, relief=FLAT, bg="#F0CFCF",
#                     font="arial 12")
# button_mul.grid(row=4, column=3, sticky=W, padx=4, pady=4)
#
# button_4 = Button(win, text="4", command=lambda: click_btn(4), padx=21, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_4.grid(row=5, column=0, sticky=W, padx=4)
#
# button_5 = Button(win, text="5", command=lambda: click_btn(5), padx=22, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_5.grid(row=5, column=1, sticky=W, padx=4)
#
# button_6 = Button(win, text="6", command=lambda: click_btn(6), padx=23, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_6.grid(row=5, column=2, sticky=W, padx=4)
#
# button_sub = Button(win, text="-", command=lambda: click_btn("-"), padx=24, pady=12, relief=FLAT, bg="#986A6A",
#                     font="arial 12")
# button_sub.grid(row=5, column=3, sticky=W, padx=4)
#
# button_1 = Button(win, text="1", command=lambda: click_btn(1), padx=21, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_1.grid(row=6, column=0, sticky=W, padx=4, pady=4)
#
# button_2 = Button(win, text="2", command=lambda: click_btn(2), padx=22, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_2.grid(row=6, column=1, sticky=W, padx=4, pady=4)
#
# button_3 = Button(win, text="3", command=lambda: click_btn(3), padx=23, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_3.grid(row=6, column=2, sticky=W, padx=4, pady=4)
#
# button_add = Button(win, text="+", command=lambda: click_btn("+"), padx=22, pady=12, relief=FLAT, bg="#F0CFCF",
#                     font="arial 12")
# button_add.grid(row=6, column=3, sticky=W, padx=4, pady=4)
#
# button_neg = Button(win, text="+/-", command=lambda: click_btn("-"), padx=17, pady=12, relief=FLAT, bg="white",
#                     font="arial 12",
#                     activebackground="#782C2C")
# button_neg.grid(row=7, column=0, sticky=W, padx=4)
#
# button_0 = Button(win, text="0", command=lambda: click_btn(0), padx=22, pady=12, relief=FLAT, bg="white",
#                   font="arial 12 bold", activebackground="#782C2C")
# button_0.grid(row=7, column=1, sticky=W, padx=4)
#
# button_dot = Button(win, text=".", command=lambda: click_btn("."), padx=25, pady=12, relief=FLAT, bg="white",
#                     font="arial 12 bold", activebackground="#782C2C")
# button_dot.grid(row=7, column=2, sticky=W, padx=4)
#
# button_eq = Button(win, text="=", command=click_equal, padx=22, pady=12, relief=FLAT, bg="#986A6A", font="arial 12")
# button_eq.grid(row=7, column=3, sticky=W, padx=4)
#
# win.mainloop()

