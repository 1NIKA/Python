import sqlite3
from matplotlib import pyplot as plt


def connect_db(base):
    return sqlite3.connect(base)


conn = connect_db("covid_dataset.sqlite")
cursor = conn.cursor()

cursor.execute(
    "SELECT SUM(new_cases) FROM covid WHERE location = 'Georgia' AND date BETWEEN '2020-06-01' AND '2020-06-30'")
for i in cursor.fetchone():
    print(i)


def total_deaths(loc, dat):
    cursor.execute("SELECT total_deaths FROM covid WHERE location = ? AND date = ?", (loc, dat))
    res1 = cursor.fetchone()[0]
    return res1


def total_deaths_per_million():
    cursor.execute("SELECT location, total_deaths_per_million FROM covid WHERE date = '2020-06-08' ORDER BY 2 DESC")
    res2 = cursor.fetchmany(5)
    return res2


print(total_deaths("Georgia", "2020-06-08"))
print(total_deaths_per_million())

date = ["ივნ 01", "ივნ 02", "ივნ 03", "ივნ 04", "ივნ 05", "ივნ 06", "ივნ 07", "ივნ 08"]

cursor.execute(
    "SELECT new_cases FROM covid WHERE location = 'Georgia' AND date BETWEEN '2020-06-01' AND '2020-06-30'")
res4 = cursor.fetchall()
cases = [item for i in res4 for item in i]

cursor.execute("SELECT new_deaths FROM covid WHERE location = 'Georgia' AND date BETWEEN '2020-06-01' AND '2020-06-30'")
res5 = cursor.fetchall()
deaths = [item for i in res5 for item in i]

plt.plot(date, cases, marker="*", ls="--", label="ახალი შემთხვევები")
plt.plot(date, deaths, marker=".", ls="-", label="გარდაცვლილი")

plt.title("კორონა ვირუსი (ივნისი)")
plt.xlabel("თარიღი")
plt.ylabel("რაოდენობა")
plt.legend()
plt.show()

'''მოცემული დიაგრამა ასახავს ივნისის თვეში ახალი შემთხვევებისა და გარდაცვლილთა რაოდენობასა.
თარიღი ჩავყარე ლისტში ჩემი ხელით იმის გამო, რომ 
ბაზიდან წამოღებული თარიღი ცუდად ჯდებოდა დიაგრამაში. ხოლო სხვა მონაცემები წამოღებულია ბაზიდან.'''

conn.close()
