# -------- დავალება 1--------
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as msg
import sqlite3
from matplotlib import pyplot as plt
import numpy as np

# win = tk.Tk()
# win.title("წიგნების აპლიკაცია")
# win.geometry("400x300+550+200")
# win.resizable(0, 0)
# win.configure(bg="white")
#
# conn = sqlite3.connect("book_db.sqlite")
# cursor = conn.cursor()
#
#
# def click_save():
#     t = title.get()
#     a = author.get()
#     p = price.get()
#     if (t and a and p) != "":
#         cursor.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", (t, a, p))
#         msg.showinfo("შეტყობინება", "მონაცემები წარმატებით დაემატა")
#     else:
#         msg.showinfo("შეცდომა", "გთხოვთ შეავსოთ ყველა ველი")
#
#
# lf1 = ttk.Labelframe(win, text="მონაცემების დამატება", labelanchor="n")
# lf1.pack(fill="both", expand=1, pady=30)
#
# lb1 = ttk.Label(lf1, text="წიგნის დასახელება:")
# lb1.grid(row=0, column=0, sticky="w", padx=10)
# title = ttk.Entry(lf1, width=30)
# title.grid(row=0, column=1, pady=10, sticky="w", padx=10)
#
# lb2 = ttk.Label(lf1, text="ავტორი:")
# lb2.grid(row=1, column=0, sticky="w", padx=10)
# author = ttk.Entry(lf1, width=20)
# author.grid(row=1, column=1, sticky="w", padx=10, pady=10)
#
# lb3 = ttk.Label(lf1, text="ფასი:")
# lb3.grid(row=2, column=0, sticky="w", padx=10)
# price = ttk.Entry(lf1, width=10)
# price.grid(row=2, column=1, sticky="w", padx=10, pady=10)
# lb4 = ttk.Label(lf1, text="ლარი")
# lb4.grid(row=2, column=1, padx=80)
#
# save = ttk.Button(lf1, text="მონაცემების დამატება", command=click_save)
# save.grid(row=3, column=0, pady=35, columnspan=2)
#
# s = ttk.Style()
# s.configure("TLabelframe", background="white")
# s.configure("TLabel", background="white")
#
# win.mainloop()
# conn.commit()
# conn.close()


# -------- დავალება 2--------
def connect_db(name):
    return sqlite3.connect(name)


conn = connect_db("Titanic.sqlite")
cursor = conn.cursor()


def count_by_gender(gender):
    cursor.execute("SELECT COUNT(*) FROM Passengers WHERE sex = ?", (gender,))
    res1 = cursor.fetchone()[0]
    print(f"გემზე იმყოფებოდა: {res1} {gender}")
    return res1


def count_by_gender_surv(gender, surv):
    cursor.execute("SELECT COUNT(*) FROM passengers WHERE sex = ? AND survived = ?", (gender, surv))
    res2 = cursor.fetchone()[0]
    print(f"სქესი: {gender}, სტატუსი: {surv}, რაოდენობა: {res2}")
    return res2


def count_by_P_class(P_class):
    cursor.execute("SELECT COUNT(*) FROM Passengers WHERE Pclass = ?", (P_class,))
    res3 = cursor.fetchone()[0]
    print(f"{P_class} კლასის ბილეთით მგზავრობდა: {res3} ადამიანი")
    return res3

def count_by_P_class_surv(P_class, surv):
    cursor.execute("SELECT COUNT(*) FROM Passengers WHERE Pclass = ? AND survived = ?", (P_class, surv))
    res4 = cursor.fetchone()[0]
    return res4

def avgPrice_by_P_class(P_class):
    cursor.execute("SELECT AVG(Fare) FROM Passengers WHERE Pclass = ?", (P_class,))
    res5 = cursor.fetchone()[0]
    print(f"{P_class} კლასის ბილეთის საშუალო ფასი არის: {round(res5, 2)}")
    return res5


def percent(x, y):
    return (x / y) * 100


cursor.execute("SELECT COUNT(*) FROM Passengers")
total = cursor.fetchone()[0]

n_female = count_by_gender("female")
n_male = count_by_gender("male")

n_female_surv = count_by_gender_surv("female", 1)
n_female_not_surv = count_by_gender_surv("female", 0)
n_male_surv = count_by_gender_surv("male", 1)
n_male_not_surv = count_by_gender_surv("male", 0)

n_P1_class = count_by_P_class(1)
n_P2_class = count_by_P_class(2)
n_P3_class = count_by_P_class(3)

count_by_P1_class_surv = count_by_P_class_surv(1, 1)
count_by_P1_class_not_surv = count_by_P_class_surv(1, 0)
count_by_P2_class_surv = count_by_P_class_surv(2, 1)
count_by_P2_class_not_surv = count_by_P_class_surv(2, 0)
count_by_P3_class_surv = count_by_P_class_surv(3, 1)
count_by_P3_class_not_surv = count_by_P_class_surv(3, 0)

avgPrice_by_P_class(1)
avgPrice_by_P_class(2)
avgPrice_by_P_class(3)

p_female = percent(n_female, total)
p_male = percent(n_male, total)
p_female_surv = percent(n_female_surv, total)
p_female_not_surv = percent(n_female_not_surv, total)
p_male_surv = percent(n_male_surv, total)
p_male_not_surv = percent(n_male_not_surv, total)
p_P1_class = percent(n_P1_class, total)
p_P2_class = percent(n_P2_class, total)
p_P3_class = percent(n_P3_class, total)

print("გემზე მყოფი ქალების პროცენტული რაოდენობა: {:.2f}%".format(p_female))
print("გემზე მყოფი კაცების პროცენტული რაოდენობა: {:.2f}%".format(p_male))
print("გადარჩენილი ქალების პროცენტული რაოდენობა: {:.2f}%".format(p_female_surv))
print("ვერ გადარჩენილი ქალების პროცენტული რაოდენობა: {:.2f}%".format(p_female_not_surv))
print("გადარჩენილი კაცების პროცენტული რაოდენობა: {:.2f}%".format(p_male_surv))
print("ვერ გადარჩენილი კაცების პროცენტული რაოდენობა: {:.2f}%".format(p_male_not_surv))
print("პირველი კლასის ბილეთების პროცენტული რაოდენობა: {:.2f}%".format(p_P1_class))
print("მეორე კლასის ბილეთების პროცენტული რაოდენობა: {:.2f}%".format(p_P2_class))
print("მესამე კლასის ბილეთების პროცენტული რაოდენობა: {:.2f}%".format(p_P3_class))

# დიაგრამა 1
labels = ["პირველი კლასი", "მეორე კლასი", "მესამე კლასი"]
sizes = [p_P1_class, p_P2_class, p_P3_class]

plt.pie(sizes, labels=labels, autopct="%1.2f%%", startangle=90)
plt.savefig("დიაგრამა2.png")

plt.show()

# დიაგრამა 2
labels2 = ["პირველი კლასი", "მეორე კლასი", "მესამე კლასი"]
num_surv = [count_by_P1_class_surv, count_by_P2_class_surv, count_by_P3_class_surv]
num_not_surv = [count_by_P1_class_not_surv, count_by_P2_class_not_surv, count_by_P3_class_not_surv]

ind = np.arange(len(labels2))
width = 0.35

rect1 = plt.bar(ind, num_surv, width, label="გადარჩა")
rect2 = plt.bar(ind + width, num_not_surv, width, label="ვერ გადარჩა")

plt.ylabel("რაოდენობა")
plt.title("ბილეთების რაოდენობა კლასების მიხედვით")
plt.xticks(ind + width / 2, labels2)
plt.legend()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                     xy=(rect.get_x() + rect.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom')


autolabel(rect1)
autolabel(rect2)

plt.savefig("დიაგრამა3.png")
plt.show()

conn.commit()
conn.close()


# --------დავალება 3--------
conn = sqlite3.connect("geo_stat.sqlite")
cursor = conn.cursor()

cursor.execute("SELECT year FROM geo_stat")
res = cursor.fetchall()
years = [item for i in res for item in i]

cursor.execute("SELECT population FROM geo_stat")
res = cursor.fetchall()
population = [item for i in res for item in i]

cursor.execute("SELECT birth FROM geo_stat")
res = cursor.fetchall()
birth = [item for i in res for item in i]

cursor.execute("SELECT marriage FROM geo_stat")
res = cursor.fetchall()
marriage = [item for i in res for item in i]

cursor.execute("SELECT divorce FROM geo_stat")
res = cursor.fetchall()
divorce = [item for i in res for item in i]

# გრაფიკი 1
plt.plot(years, population, marker="o", ls="--", label="მოსახლეობა")

plt.title("პოპულაცია")
plt.xlabel("წელი")
plt.ylabel("რაოდენობა (მილიონებში)")
plt.legend()
plt.xticks(years)
plt.show()

# გრაფიკი 2
plt.plot(years, birth, marker=".", ls=":", color="y")

plt.title("შობადობა")
plt.xlabel("წელი")
plt.ylabel("რაოდენობა")
plt.show()

# გრაფიკი 3
plt.plot(years, marriage, marker="*", ls="--", label="დაქორწინებული")
plt.plot(years, divorce, marker=".", ls="-", label="განქორწინებული")

plt.title("ქორწინება/განქორწინების გრაფიკი")
plt.xlabel("წელი")
plt.ylabel("რაოდენობა")
plt.legend()
plt.show()

conn.commit()
conn.close()
