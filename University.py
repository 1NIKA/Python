# -------- დავალება 1--------
import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.geometry("400x520+580+100")
win.title("სასწავლო წიგნაკი")
win.iconbitmap(r"ico file\BTU.ico")

dic = {}
Registration = open(r"C:\Users\kldia\.android\python\Registration.txt", "a", encoding="UTF-8")


def click_add():
    dic["სახელი"] = name.get()
    dic["გვარი"] = sur_name.get()
    dic["დაბ.თარიღი"] = f"{c1.get()} {c2.get()} {c3.get()}"
    dic["E-mail"] = email.get()
    dic["ტელეფონი"] = tel.get()
    dic["ფაკულტეტი"] = c4.get()
    dic["საფეხური"] = c5.get()
    dic["კურსი"] = c6.get()
    Registration.write(str(dic) + "\n")
    print(dic)


def click_reset():
    name.delete(0, tkinter.END)
    sur_name.delete(0, tkinter.END)
    c1.set("წელი")
    c2.set("თვე")
    c3.set("დღე")
    email.delete(0, tkinter.END)
    tel.delete(0, tkinter.END)
    c4.set("აირჩიეთ ფაკულტეტი")
    c5.set("აირჩიეთ საფეხური")
    c6.set("აირჩიეთ კურსი")


def click_destroy():
    win.destroy()


def choose_course():
    if c5.current() == 0:
        c6["values"] = ["პროგრამირება Python", "Cisco Packet Tracer", "მობილური აპლიკაციები", "მონაცემთა ბაზები"]
    elif c5.current() == 1:
        c6["values"] = ["IT-სერვისების მართვა", "ფინანსური აღრიცხვა"]
    elif c5.current() == 2:
        c6["values"] = ["აკადემიური წერა", "სტატისტიკა", "პროსპექტუსი", "ემპირიული მეთოდები", "კვლევის მეთოდები"]


nb = ttk.Notebook(win)
nb.pack(fill="both", expand=1, padx=10, pady=10)

tab1 = ttk.Frame(nb)
tab2 = ttk.Frame(nb)
tab3 = ttk.Frame(nb)

nb.add(tab1, text="Registration", underline=0)
nb.add(tab2, text="All Students", underline=0)
nb.add(tab3, text="Lectures", underline=0)

lb1 = ttk.LabelFrame(tab1, text="პირადი ინფორმაცია")
lb1.pack(fill="both", expand=1, pady=15, padx=10)

ttk.Label(lb1, text="სახელი: ").grid(row=0, column=0, padx=10, pady=5, sticky="w")
ttk.Label(lb1, text="გვარი: ").grid(row=1, column=0, padx=10, pady=5, sticky="w")
ttk.Label(lb1, text="დაბ.თარიღი:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
ttk.Label(lb1, text="სქესი: ").grid(row=3, column=0, padx=10, pady=5, sticky="w")
ttk.Label(lb1, text="E-mail: ").grid(row=4, column=0, padx=10, pady=5, sticky="w")
ttk.Label(lb1, text="ტელ : ").grid(row=5, column=0, padx=10, pady=5, sticky="w")
tkinter.Label(tab2, text="პირადი მონაცემების გავრცელების უფლება არ გვაქვს!", fg="purple").grid(row=0, column=0,
                                                                                               pady=200, padx=20)
tkinter.Label(tab3, text="დაფარულია ადმინისტრაციის მიერ!", fg="purple").grid(row=0, column=0, pady=200, padx=75)

name = ttk.Entry(lb1)
name.grid(row=0, column=1, padx=20, ipadx=30, columnspan=3)
sur_name = ttk.Entry(lb1)
sur_name.grid(row=1, column=1, padx=20, pady=5, ipadx=30, columnspan=3)
email = ttk.Entry(lb1)
email.grid(row=4, column=1, padx=20, pady=5, ipadx=30, columnspan=3)
tel = ttk.Entry(lb1)
tel.grid(row=5, column=1, padx=20, pady=5, ipadx=30, columnspan=3)

var1 = tkinter.StringVar()
var1.set("წელი")
c1 = ttk.Combobox(lb1, textvariable=var1, width=7, state="readonly")
c1["values"] = [2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990]
c1.grid(row=2, column=1, padx=19, sticky="w")
var2 = tkinter.StringVar()
var2.set("თვე")
c2 = ttk.Combobox(lb1, textvariable=var2, width=4, state="readonly")
c2["values"] = ["იან", "თებ", "მარ", "აპრ", "მაი", "ივნ", "ივლ", "აგვ", "სექ", "ოქტ", "ნოე", "დეკ"]
c2.grid(row=2, column=2, sticky="w")
var3 = tkinter.StringVar()
var3.set("დღე")
c3 = ttk.Combobox(lb1, textvariable=var3, width=5, state="readonly")
c3["values"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31]
c3.grid(row=2, column=3, padx=10, sticky="w")

rd1 = ttk.Radiobutton(lb1, text="ქალი", value=1)
rd1.grid(row=3, column=1)
rd1 = ttk.Radiobutton(lb1, text="კაცი", value=2)
rd1.grid(row=3, column=2)

lb2 = ttk.LabelFrame(tab1, text="უნივერსიტეტი")
lb2.pack(fill="both", expand=1, pady=15, padx=10)

ttk.Label(lb2, text="ფაკულტეტი: ").grid(row=0, column=0, padx=10, pady=5, sticky="w")
ttk.Label(lb2, text="საფეხური: ").grid(row=1, column=0, padx=10, pady=5, sticky="w")
ttk.Label(lb2, text="კურსი: ").grid(row=2, column=0, padx=10, pady=5, sticky="w")

var4 = tkinter.StringVar()
var4.set("აირჩიეთ ფაკულტეტი")
c4 = ttk.Combobox(lb2, textvariable=var4, width=18, state="readonly")
c4["values"] = ["კომპიუტერული მეცნიერება", "მენეჯმენტი", "ფინანსები"]
c4.grid(row=0, column=1, padx=16, pady=5, ipadx=31, columnspan=3)
var5 = tkinter.StringVar()
var5.set("აირჩიეთ საფეხური")
c5 = ttk.Combobox(lb2, textvariable=var5, width=18, state="readonly")
c5["values"] = ["ბაკალავრიატი", "მაგისტრატურა", "დოქტორანტურა"]
c5.grid(row=1, column=1, padx=16, pady=10, ipadx=31, columnspan=3)
var6 = tkinter.StringVar()
var6.set("აირჩიეთ კურსი")
c6 = ttk.Combobox(lb2, textvariable=var6, width=18, state="readonly", postcommand=choose_course)
c6.grid(row=2, column=1, padx=16, pady=5, ipadx=31, columnspan=3)

add = ttk.Button(tab1, text="დამატება", command=click_add)
add.pack(side="left", padx=15)
reset = ttk.Button(tab1, text="Reset", command=click_reset)
reset.pack(side="left", padx=15)
destroy = ttk.Button(tab1, text="ფანჯრის დახურვა", command=click_destroy)
destroy.pack(side="left", padx=15)

nb.enable_traversal()
win.mainloop()
