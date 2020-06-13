import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

win = tk.Tk()
win.geometry("500x400+500+150")
win.title("მთავარი გვერდი")
win.iconbitmap(r"ico file\BTU.ico")
win.resizable(0, 0)
win.configure(bg="white")

img = tk.PhotoImage(file="img/btu_logo.png")
img = img.subsample(3)

var8 = tk.StringVar()
var8.set("თეთრი")

# მომხმარებლის მეილი და პაროლი
mail1 = "nika.kldiashvili.2@btu.edu.ge"
pas = "nika123"

file = open("NewUsers.txt", "a", encoding="UTF-8")
file1 = open("NewCourses.txt", "a", encoding="UTF-8")
d = {}
d1 = {}


def click_save():
    if var2.get() == 0 and var3.get() == 0 and var4.get() == 0 and var5.get() == 0 and var6.get() == 0 and \
            var7.get() == 0:
        msg.showinfo("ინფორმაცია", "გთხოვთ აირჩიოთ მინიმუმ ერთი კურსი!")
    else:
        d1["ეკონომიკის პრინციპები"] = var2.get()
        d1["ფინანსური აღრიცხვის საფუძვლები"] = var3.get()
        d1["დაზღვევა"] = var4.get()
        d1["კომპიუტერული ქსელების საწყისები"] = var5.get()
        d1["ეკონომიკის საფუძვლები"] = var6.get()
        d1["კომპიუტერული ქსელები (CCNA 1)"] = var7.get()
        msg.showinfo("ინფორმაცია", "კურსების დამატებაზე მოთხოვნა გაგზავნილია")
        file1.write(str(d1) + "\n")


def change_language():
    if combo.current() == 1:
        win3.configure(bg="#BBB9B8")
        s.configure("TButton", foreground="blue", font=("arial", 11))
        s.configure("TLabelframe", background="#BBB9B8", font=("arial", 10))
        s.configure("TFrame", background="#BBB9B8")
        s.configure("TLabel", background="#BBB9B8", font=("arial", 10))
        s.configure("TRadiobutton", background="white", font=("arial", 10, "bold"))
        s.configure("lb1.TLabel", foreground="#B11300", font=("arial", 12))
        s.configure("lb2.TLabel", font=("arial", 10, "bold"))
        s.configure("lb3.TLabel", foreground="#10258E")
        s.configure("TCheckbutton", background="#BBB9B8")
    elif combo.current() == 0:
        win3.configure(bg="white")
        s.configure("TButton", foreground="blue", font=("arial", 11))
        s.configure("TLabelframe", background="white", font=("arial", 10))
        s.configure("TFrame", background="white")
        s.configure("TLabel", background="white", font=("arial", 10))
        s.configure("TRadiobutton", background="white", font=("arial", 10, "bold"))
        s.configure("lb1.TLabel", foreground="#B11300", font=("arial", 12))
        s.configure("lb2.TLabel", font=("arial", 10, "bold"))
        s.configure("lb3.TLabel", foreground="#10258E")
        s.configure("TCheckbutton", background="white")


def click_enter():
    if mail.get() == mail1 and password.get() == pas:
        mail.delete(0, tk.END)
        password.delete(0, tk.END)
        global win3
        win3 = tk.Toplevel()
        win3.title("Classroom")
        win3.geometry("500x600+500+100")
        win3.iconbitmap(r"ico file\BTU.ico")
        win3.configure(bg="white")
        ttk.Label(win3, image=img).grid(row=0, column=0, rowspan=2, sticky="w")

        ttk.Label(win3, text="ნიკა კლდიაშვილი").grid(row=2, column=0, sticky="w", padx=10)
        ttk.Label(win3, text="ინფორმაციული ტექნოლოგიები").grid(row=3, column=0, sticky="w", columnspan=3, padx=10)
        ttk.Label(win3, text="BTU Classroom", style="lb1.TLabel").grid(row=0, column=1, sticky="w", padx=100)

        nb = ttk.Notebook(win3)
        nb.grid(row=4, column=0, pady=40, columnspan=4, sticky="w", padx=22)

        tab1 = ttk.Frame(nb)
        tab2 = ttk.Frame(nb)
        tab3 = ttk.Frame(nb)
        tab4 = ttk.Frame(nb)

        nb.add(tab1, text="არჩეული კურსები")
        nb.add(tab2, text="ცხრილი")
        nb.add(tab3, text="ლექტორების სია")
        nb.add(tab4, text="დამატებითი კურსები")

        ttk.Label(tab1, text="კურსები", style="lb2.TLabel").grid(row=0, column=0, pady=12, padx=10, sticky="w")
        ttk.Label(tab1, text="მენეჯმენტის საფუძვლები", style="lb3.TLabel").grid(row=1, column=0, pady=12, padx=10,
                                                                                sticky="w")
        ttk.Label(tab1, text="პერსონალური კომპიუტერის არქიტექტურა", style="lb3.TLabel").grid(row=2, column=0, pady=12,
                                                                                             padx=10, sticky="w")
        ttk.Label(tab1, text="მათემატიკა 2", style="lb3.TLabel").grid(row=3, column=0, pady=12, padx=10, sticky="w")
        ttk.Label(tab1, text="მონაცემთა ბაზების საწყისები", style="lb3.TLabel").grid(row=4, column=0, pady=12, padx=10,
                                                                                     sticky="w")
        ttk.Label(tab1, text="პროგრამირება Python", style="lb3.TLabel").grid(row=5, column=0, pady=12, padx=10,
                                                                             sticky="w")
        ttk.Label(tab1, text="ინოვაციების მენეჯმენტი და სტარტაპი", style="lb3.TLabel").grid(row=6, column=0, pady=12,
                                                                                            padx=10, sticky="w")
        ttk.Label(tab1, text="მობილური აპლიკაციები", style="lb3.TLabel").grid(row=7, column=0, pady=12, padx=10,
                                                                              sticky="w")

        ttk.Label(tab1, text="კრედ", style="lb2.TLabel").grid(row=0, column=1, pady=12, padx=65)
        ttk.Label(tab1, text=6, style="lb3.TLabel").grid(row=1, column=1, pady=12, padx=65)
        ttk.Label(tab1, text=4, style="lb3.TLabel").grid(row=2, column=1, pady=12, padx=65)
        ttk.Label(tab1, text=5, style="lb3.TLabel").grid(row=3, column=1, pady=12, padx=65)
        ttk.Label(tab1, text=3, style="lb3.TLabel").grid(row=4, column=1, pady=12, padx=65)
        ttk.Label(tab1, text=6, style="lb3.TLabel").grid(row=5, column=1, pady=12, padx=65)
        ttk.Label(tab1, text=6, style="lb3.TLabel").grid(row=6, column=1, pady=12, padx=65)
        ttk.Label(tab1, text=3, style="lb3.TLabel").grid(row=7, column=1, pady=12, padx=65)

        ttk.Label(tab3, text="ლექტორები", style="lb2.TLabel").grid(row=0, column=0, pady=12, padx=10, sticky="w")
        ttk.Label(tab3, text="სალომე სილაგაძე").grid(row=1, column=0, pady=12, padx=10, sticky="w")
        ttk.Label(tab3, text="ირაკლი ჟღენტი").grid(row=2, column=0, pady=12, padx=10, sticky="w")
        ttk.Label(tab3, text="რევაზ ციცქიშვილი").grid(row=3, column=0, pady=12, padx=10, sticky="w")
        ttk.Label(tab3, text="იოსებ ბერიძე").grid(row=4, column=0, pady=12, padx=10, sticky="w")
        ttk.Label(tab3, text="ლიკა სვანაძე").grid(row=5, column=0, pady=12, padx=10, sticky="w")
        ttk.Label(tab3, text="თამთა გველესიანი").grid(row=6, column=0, pady=12, padx=10, sticky="w")
        ttk.Label(tab3, text="სოსო ნინიძე").grid(row=7, column=0, pady=12, padx=10, sticky="w")

        ttk.Label(tab3, text="ელ.ფოსტა", style="lb2.TLabel").grid(row=0, column=1, pady=12, sticky="w", padx=67)
        ttk.Label(tab3, text="Salome.Silagadze@btu.edu.ge", style="lb3.TLabel").grid(row=1, column=1, pady=12,
                                                                                     sticky="w", padx=67)
        ttk.Label(tab3, text="irakli.zhgenti@btu.edu.ge", style="lb3.TLabel").grid(row=2, column=1, pady=12, sticky="w",
                                                                                   padx=67)
        ttk.Label(tab3, text="revaz.tsitskishvili@btu.edu.ge", style="lb3.TLabel").grid(row=3, column=1, pady=12,
                                                                                        sticky="w", padx=67)
        ttk.Label(tab3, text="Ioseb.Beridze@btu.edu.ge", style="lb3.TLabel").grid(row=4, column=1, pady=12, sticky="w",
                                                                                  padx=67)
        ttk.Label(tab3, text="lika.svanadze@btu.edu.ge", style="lb3.TLabel").grid(row=5, column=1, pady=12, sticky="w",
                                                                                  padx=67)
        ttk.Label(tab3, text="tamta.gvelesiani@btu.edu.ge", style="lb3.TLabel").grid(row=6, column=1, pady=12,
                                                                                     sticky="w", padx=67)
        ttk.Label(tab3, text="soso.ninidze@btu.edu.ge", style="lb3.TLabel").grid(row=7, column=1, pady=12, sticky="w",
                                                                                 padx=67)

        tk.Label(tab2, text="ორშაბათი", bg="#8397FA", width=64).grid(row=0, column=0, columnspan=5)
        ttk.Label(tab2, text="17:00 - 17:50   პროგრამირება Python").grid(row=1, column=0, sticky="w")
        ttk.Label(tab2, text="18:00 - 18:50   პროგრამირება Python").grid(row=2, column=0, sticky="w")
        ttk.Label(tab2, text="19:00 - 19:50   მონაცემთა ბაზების საწყისები").grid(row=3, column=0, sticky="w")
        ttk.Label(tab2, text="20:00 - 20:50   მონაცემთა ბაზების საწყისები").grid(row=4, column=0, sticky="w")
        tk.Label(tab2, text="სამშაბათი", bg="#8397FA", width=64).grid(row=5, column=0, columnspan=5)
        ttk.Label(tab2, text="09:00 - 09:50   მენეჯმენტის საფუძვლები").grid(row=6, column=0, sticky="w")
        ttk.Label(tab2, text="10:00 - 10:50   მენეჯმენტის საფუძვლები").grid(row=7, column=0, sticky="w")
        tk.Label(tab2, text="ოთხშაბათი", bg="#8397FA", width=64).grid(row=8, column=0, columnspan=5)
        ttk.Label(tab2, text="19:00 - 19:50   ინოვაციების მენეჯმენტი და სტარტაპი").grid(row=9, column=0, sticky="w")
        ttk.Label(tab2, text="20:00 - 20:50   ინოვაციების მენეჯმენტი და სტარტაპი").grid(row=10, column=0, sticky="w")
        tk.Label(tab2, text="ხუთშაბათი", bg="#8397FA", width=64).grid(row=11, column=0, columnspan=5)
        ttk.Label(tab2, text="19:00 - 19:50   პერსონალური კომპიუტერის არქიტექტურა").grid(row=12, column=0, sticky="w")
        ttk.Label(tab2, text="20:00 - 20:50   პერსონალური კომპიუტერის არქიტექტურა").grid(row=13, column=0, sticky="w")
        tk.Label(tab2, text="პარასკევი", bg="#8397FA", width=64).grid(row=14, column=0, columnspan=5)
        ttk.Label(tab2, text="09:00 - 09:50   მათემატიკა 2").grid(row=15, column=0, sticky="w")
        ttk.Label(tab2, text="10:00 - 10:50   მათემატიკა 2").grid(row=16, column=0, sticky="w")

        global var2
        var2 = tk.IntVar()
        global var3
        var3 = tk.IntVar()
        global var4
        var4 = tk.IntVar()
        global var5
        var5 = tk.IntVar()
        global var6
        var6 = tk.IntVar()
        global var7
        var7 = tk.IntVar()
        c1 = ttk.Checkbutton(tab4, text="ეკონომიკის პრინციპები", variable=var2, style="TCheckbutton")
        c1.grid(row=0, column=0, pady=12, padx=20, sticky="w")
        c2 = ttk.Checkbutton(tab4, text="ფინანსური აღრიცხვის საფუძვლები", variable=var3, style="TCheckbutton")
        c2.grid(row=1, column=0, pady=12, padx=20, sticky="w")
        c3 = ttk.Checkbutton(tab4, text="დაზღვევა", variable=var4, style="TCheckbutton")
        c3.grid(row=2, column=0, pady=12, padx=20, sticky="w")
        c4 = ttk.Checkbutton(tab4, text="კომპიუტერული ქსელების საწყისები", variable=var5, style="TCheckbutton")
        c4.grid(row=3, column=0, pady=12, padx=20, sticky="w")
        c5 = ttk.Checkbutton(tab4, text="ეკონომიკის საფუძვლები", variable=var6, style="TCheckbutton")
        c5.grid(row=4, column=0, pady=12, padx=20, sticky="w")
        c6 = ttk.Checkbutton(tab4, text="კომპიუტერული ქსელები (CCNA 1)", variable=var7, style="TCheckbutton")
        c6.grid(row=5, column=0, pady=12, padx=20, sticky="w")

        save = ttk.Button(tab4, text="კურსების დამატება", command=click_save)
        save.grid(row=6, column=0, pady=23, padx=110, ipadx=30)
        save.bind("<Button-1>", save_position)

        global combo
        combo = ttk.Combobox(win3, textvariable=var8, state="readonly", postcommand=change_language)
        combo["values"] = ["თეთრი", "მუქი"]
        combo.grid(row=3, column=1, padx=170)
    else:
        msg.showerror("შეცდომა", "მომხმარებლის ელ.ფოსტა ან პაროლი არასწორია")
        password.delete(0, tk.END)


def save_position(event):
    print(event.x, event.y)


def click_reg():
    if reg_mail.get() == "":
        msg.showerror("გაფრთხილება", "გთხოვთ შეავსოთ ყველა ველი")
    elif reg_password.get() == "":
        msg.showerror("გაფრთხილება", "გთხოვთ შეავსოთ ყველა ველი")
    elif var1.get() == 0:
        msg.showerror("გაფრთხილება", "გთხოვთ შეავსოთ ყველა ველი")
    elif reg_mail.get() == "" and reg_password.get() == "":
        msg.showerror("გაფრთხილება", "გთხოვთ შეავსოთ ყველა ველი")
    elif reg_mail.get() == "" and var1.get() == 0:
        msg.showerror("გაფრთხილება", "გთხოვთ შეავსოთ ყველა ველი")
    elif reg_password.get() == "" and var1.get() == 0:
        msg.showerror("გაფრთხილება", "გთხოვთ შეავსოთ ყველა ველი")
    elif reg_password.get() == "" and reg_password.get() == "" and var1.get() == 0:
        msg.showerror("გაფრთხილება", "გთხოვთ შეავსოთ ყველა ველი")
    else:
        d["mail"] = reg_mail.get()
        d["password"] = reg_password.get()
        d["gender"] = var1.get()
        msg.showinfo("რეგისტრაცია", "თქვენ წარმატებით დარეგისტრირდით!")
        file.write(str(d) + "\n")


def click_registration():
    win2 = tk.Toplevel()
    win2.title("რეგისტრაცია")
    win2.geometry("500x400+500+150")
    win2.iconbitmap(r"ico file\BTU.ico")
    win2.configure(bg="white")

    lb3 = ttk.Frame(win2)
    lb3.pack(fill="both", expand=1, pady=15, padx=10)
    lb4 = ttk.LabelFrame(lb3, text="რეგისტრაცია", labelanchor="n")
    lb4.pack(fill="both", expand=1, pady=70, padx=50)

    ttk.Label(lb4, text="ელფოსტა*:").grid(row=0, column=0, padx=95, pady=10, columnspan=2, sticky="w")
    ttk.Label(lb4, text="პაროლი*:").grid(row=2, column=0, padx=95, pady=10, columnspan=2, sticky="w")

    global reg_mail
    reg_mail = ttk.Entry(lb4)
    reg_mail.grid(row=1, column=0, sticky="w", padx=95, ipadx=30, columnspan=2)
    reg_mail.bind("<Return>", register)
    global reg_password
    reg_password = ttk.Entry(lb4)
    reg_password.grid(row=3, column=0, sticky="w", padx=95, ipadx=30, columnspan=2)
    reg_password.bind("<Return>", register)

    global var1
    var1 = tk.IntVar()
    rd1 = ttk.Radiobutton(lb4, text="ქალი", variable=var1, value=1, style="TRadiobutton")
    rd1.grid(row=4, column=0, pady=15, sticky="w", padx=120, columnspan=2)
    rd2 = ttk.Radiobutton(lb4, text="კაცი", variable=var1, value=2, style="TRadiobutton")
    rd2.grid(row=4, column=1, pady=15, sticky="w", columnspan=2, padx=15)

    reg = ttk.Button(lb4, text="რეგისტრაცია", command=click_reg)
    reg.grid(row=5, column=0, columnspan=2, sticky="w", padx=107, ipadx=30)


def register(event):
    return click_reg()


def enter(event):
    return click_enter()


s = ttk.Style()
s.configure("TButton", foreground="blue", font=("arial", 11))
s.configure("TLabelframe", background="white", font=("arial", 10))
s.configure("TFrame", background="white")
s.configure("TLabel", background="white", font=("arial", 10))
s.configure("TRadiobutton", background="white", font=("arial", 10, "bold"))
s.configure("lb1.TLabel", foreground="#B11300", font=("arial", 12))
s.configure("lb2.TLabel", font=("arial", 10, "bold"))
s.configure("lb3.TLabel", foreground="#10258E")
s.configure("TCheckbutton", background="white")

lb1 = ttk.Frame(win)
lb1.pack(fill="both", expand=1, pady=15, padx=10)
lb2 = ttk.LabelFrame(lb1, text="ავტორიზაცია", labelanchor="n")
lb2.pack(fill="both", expand=1, pady=70, padx=50)

ttk.Label(lb2, text="ელფოსტა*:").grid(row=0, column=0, padx=95, pady=10, columnspan=2, sticky="w")
ttk.Label(lb2, text="პაროლი*:").grid(row=2, column=0, padx=95, pady=10, columnspan=2, sticky="w")

mail = ttk.Entry(lb2)
mail.grid(row=1, column=0, sticky="w", padx=95, ipadx=30, columnspan=2)
password = ttk.Entry(lb2, show="*")
password.grid(row=3, column=0, sticky="w", padx=95, ipadx=30, columnspan=2)

mail.bind("<Return>", enter)
password.bind("<Return>", enter)

enter = ttk.Button(lb2, text="შესვლა", command=click_enter)
enter.grid(row=4, column=0, columnspan=2, sticky="w", padx=80)
registration = ttk.Button(lb2, text="რეგისტრაცია", command=click_registration)
registration.grid(row=4, column=1, columnspan=2, sticky="w", padx=6, pady=20)

win.mainloop()
