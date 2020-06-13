import tkinter as tk
from tkinter import ttk


class Health:
    def __init__(self, age, sex, pulse):
        self.age = age
        self.sex = sex
        self.pulse = pulse

    def __str__(self):
        return f"ასაკი: {self.age} წლის; სქესი: {self.sex}; პულსი: {self.pulse} დარტყმა/წუთში."

    def avg(self):
        d = self.pulse * 1440
        return f"{round((2600000000 / d) / 365, 2)} წელი"

    def max_pulse(self):
        if self.sex == "F":
            return f"{226 - (0.9 * self.age)} წუთში"
        elif self.sex == "M":
            return f"{223 - (0.9 * self.age)} წუთში"

    def max_pulse2(self, intensive=0.8, average=0.6, beginner=0.5):
        if self.sex == "F":
            max_pulse = f"{(226 - (0.9 * self.age) - self.pulse) * intensive + self.pulse} წუთში"
            return max_pulse
        elif self.sex == "M":
            max_pulse2 = f"{(223 - (0.9 * self.age) - self.pulse) * intensive + self.pulse} წუთში"
            return max_pulse2


h1 = Health(24, "F", 70)
print(h1.avg())
print(h1.max_pulse())
print(h1.max_pulse2())
print(h1)


def click_result():
    global f
    a = float(age1.get())
    s = var.get()
    p = float(pulse1.get())
    h2 = Health(a, s, p)
    var1.set(h2.avg())
    if s == 1:
        f = 226 - (0.9 * a)
        if cb1.current() == 0:
            var3.set(f"{(f - p) * 0.8 + p}")
        if cb1.current() == 1:
            var3.set((f - p) * 0.6 + p)
        if cb1.current() == 2:
            var3.set((f - p) * 0.5 + p)
        var2.set(f)
    else:
        m = 223 - (0.9 * a)
        if cb1.current() == 0:
            var3.set((m - p) * 0.8 + p)
        if cb1.current() == 1:
            var3.set((m - p) * 0.6 + p)
        if cb1.current() == 2:
            var3.set((m - p) * 0.5 + p)
        var2.set(m)


win = tk.Tk()
win.title("Heart Rate Calculator")
win.geometry("400x300+500+200")

ttk.Label(win, text="ასაკი: ").grid(row=0, column=0, padx=10, pady=10, sticky="w")
ttk.Label(win, text="სქესი: ").grid(row=1, column=0, padx=10, sticky="w")
ttk.Label(win, text="ნორმ.პულსი: ").grid(row=2, column=0, padx=10, pady=10, sticky="w")
ttk.Label(win, text="ვარჯიშის ტიპი: ").grid(row=3, column=0, padx=10, sticky="w")
ttk.Label(win, text="წლის").grid(row=0, column=2, padx=10, sticky="w")
ttk.Label(win, text="წუთში").grid(row=2, column=2, padx=10, sticky="w")

ttk.Label(win, text="სიცოცხლის საშ.ხანგრძლივობა: ").grid(row=5, column=0, padx=10, sticky="w", pady=10, columnspan=3)
ttk.Label(win, text="მაქსიმალური პულსი: ").grid(row=6, column=0, padx=10, sticky="w", columnspan=3)
ttk.Label(win, text="მაქს.პულსი ვარჯიშისას: ").grid(row=7, column=0, padx=10, sticky="w", pady=10, columnspan=3)

var1 = tk.StringVar()
var1.set("")
ttk.Label(win, textvariable=var1).grid(row=5, column=4)
var2 = tk.StringVar()
var2.set("")
ttk.Label(win, textvariable=var2).grid(row=6, column=4)
var3 = tk.StringVar()
var3.set("")
ttk.Label(win, textvariable=var3).grid(row=7, column=4)

age1 = ttk.Entry(win, width=6)
age1.grid(row=0, column=1)
pulse1 = ttk.Entry(win, width=6)
pulse1.grid(row=2, column=1)

var = tk.IntVar()
r1 = ttk.Radiobutton(win, text="F", variable=var, value=1)
r1.grid(row=1, column=1)
r2 = ttk.Radiobutton(win, text="M", variable=var, value=2)
r2.grid(row=1, column=2)

var4 = tk.StringVar()
var4.set("აირჩიეთ")
cb1 = ttk.Combobox(win, width=13, textvariable=var4)
cb1["values"] = ["Intensive", "Average", "Beginner"]
cb1.grid(row=3, column=1, columnspan=2, sticky="w")

result = ttk.Button(win, text="გამოთვლა", command=click_result)
result.grid(row=4, column=0, columnspan=3, pady=10, sticky="w", padx=25)

win.mainloop()


